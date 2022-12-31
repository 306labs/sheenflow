from collections import defaultdict

from dagster import DependencyDefinition, Int, NodeInvocation
from sheenflow._legacy import (
    InputDefinition,
    PipelineDefinition,
    execute_pipeline,
    lambda_solid,
    solid,
)


def test_aliased_solids():
    @lambda_solid()
    def first():
        return ["first"]

    @lambda_solid(input_defs=[InputDefinition(name="prev")])
    def not_first(prev):
        return prev + ["not_first"]

    pipeline = PipelineDefinition(
        solid_defs=[first, not_first],
        name="test",
        dependencies={
            "not_first": {"prev": DependencyDefinition("first")},
            NodeInvocation("not_first", alias="second"): {
                "prev": DependencyDefinition("not_first")
            },
            NodeInvocation("not_first", alias="third"): {"prev": DependencyDefinition("second")},
        },
    )

    result = execute_pipeline(pipeline)
    assert result.success
    solid_result = result.result_for_node("third")
    assert solid_result.output_value() == [
        "first",
        "not_first",
        "not_first",
        "not_first",
    ]


def test_only_aliased_solids():
    @lambda_solid()
    def first():
        return ["first"]

    @lambda_solid(input_defs=[InputDefinition(name="prev")])
    def not_first(prev):
        return prev + ["not_first"]

    pipeline = PipelineDefinition(
        solid_defs=[first, not_first],
        name="test",
        dependencies={
            NodeInvocation("first", alias="the_root"): {},
            NodeInvocation("not_first", alias="the_consequence"): {
                "prev": DependencyDefinition("the_root")
            },
        },
    )

    result = execute_pipeline(pipeline)
    assert result.success
    solid_result = result.result_for_node("the_consequence")
    assert solid_result.output_value() == ["first", "not_first"]


def test_aliased_configs():
    @solid(input_defs=[], config_schema=Int)
    def load_constant(context):
        return context.solid_config

    pipeline = PipelineDefinition(
        solid_defs=[load_constant],
        name="test",
        dependencies={
            NodeInvocation(load_constant.name, "load_a"): {},
            NodeInvocation(load_constant.name, "load_b"): {},
        },
    )

    result = execute_pipeline(
        pipeline, {"solids": {"load_a": {"config": 2}, "load_b": {"config": 3}}}
    )

    assert result.success
    assert result.result_for_node("load_a").output_value() == 2
    assert result.result_for_node("load_b").output_value() == 3


def test_aliased_solids_context():
    record = defaultdict(set)

    @solid
    def log_things(context):
        solid_value = context.solid.name
        op_def_value = context.op_def.name
        record[op_def_value].add(solid_value)

    pipeline = PipelineDefinition(
        solid_defs=[log_things],
        name="test",
        dependencies={
            NodeInvocation("log_things", "log_a"): {},
            NodeInvocation("log_things", "log_b"): {},
        },
    )

    result = execute_pipeline(pipeline)
    assert result.success

    assert dict(record) == {"log_things": set(["log_a", "log_b"])}
