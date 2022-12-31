# pylint: disable=redefined-outer-name
import logging
import time

from sheenflow import DagsterEvent, DagsterEventType, EventLogEntry
from sheenflow._core.execution.api import create_execution_plan
from sheenflow._core.execution.plan.resume_retry import ReexecutionStrategy
from sheenflow._core.instance import DagsterInstance
from sheenflow._core.snap import snapshot_from_execution_plan
from sheenflow._core.storage.pipeline_run import RunsFilter
from sheenflow._core.storage.tags import MAX_RETRIES_TAG, RETRY_STRATEGY_TAG
from sheenflow._core.test_utils import create_run_for_test, instance_for_test
from sheenflow._daemon.auto_run_reexecution.auto_run_reexecution import (
    consume_new_runs_for_automatic_reexecution,
    filter_runs_to_should_retry,
    get_reexecution_strategy,
)
from sheenflow._daemon.auto_run_reexecution.event_log_consumer import EventLogConsumerDaemon
from sheenflow._legacy import DagsterRunStatus

from .utils import foo, get_foo_job_handle


def create_run(instance, **kwargs):
    with get_foo_job_handle(instance) as handle:
        execution_plan = create_execution_plan(foo)
        return create_run_for_test(
            instance,
            mode="default",
            external_pipeline_origin=handle.get_external_origin(),
            pipeline_code_origin=handle.get_python_origin(),
            pipeline_name=handle.job_name,
            pipeline_snapshot=foo.get_pipeline_snapshot(),
            execution_plan_snapshot=snapshot_from_execution_plan(
                execution_plan, foo.get_pipeline_snapshot_id()
            ),
            **kwargs,
        )


def test_filter_runs_to_should_retry(instance):
    instance.wipe()

    run = create_run(instance, status=DagsterRunStatus.STARTED)

    assert list(filter_runs_to_should_retry([run], instance, 2)) == []

    dagster_event = DagsterEvent(
        event_type_value=DagsterEventType.PIPELINE_FAILURE.value,
        pipeline_name="foo",
        message="",
    )
    event_record = EventLogEntry(
        user_message="",
        level=logging.ERROR,
        pipeline_name="foo",
        run_id=run.run_id,
        error_info=None,
        timestamp=time.time(),
        dagster_event=dagster_event,
    )
    instance.handle_new_event(event_record)

    assert (
        len(
            list(
                filter_runs_to_should_retry(
                    instance.get_runs(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
                    instance,
                    2,
                )
            )
        )
        == 1
    )


def test_filter_runs_to_should_retry_tags(instance):
    instance.wipe()

    run = create_run(instance, status=DagsterRunStatus.STARTED, tags={MAX_RETRIES_TAG: "0"})

    assert list(filter_runs_to_should_retry([run], instance, 2)) == []

    instance.report_run_failed(run)

    assert (
        len(
            list(
                filter_runs_to_should_retry(
                    instance.get_runs(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
                    instance,
                    2,
                )
            )
        )
        == 0
    )

    instance.wipe()

    run = create_run(instance, status=DagsterRunStatus.STARTED, tags={MAX_RETRIES_TAG: "10"})

    assert list(filter_runs_to_should_retry([run], instance, 0)) == []

    instance.report_run_failed(run)

    assert (
        len(
            list(
                filter_runs_to_should_retry(
                    instance.get_runs(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
                    instance,
                    2,
                )
            )
        )
        == 1
    )

    instance.wipe()

    run = create_run(
        instance, status=DagsterRunStatus.STARTED, tags={MAX_RETRIES_TAG: "not-an-int"}
    )

    assert list(filter_runs_to_should_retry([run], instance, 0)) == []

    instance.report_run_failed(run)

    assert (
        list(
            filter_runs_to_should_retry(
                instance.get_runs(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
                instance,
                2,
            )
        )
        == []
    )


def test_consume_new_runs_for_automatic_reexecution(instance, workspace_context):
    instance.wipe()
    instance.run_coordinator.queue().clear()

    list(
        consume_new_runs_for_automatic_reexecution(
            workspace_context,
            instance.get_run_records(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
        )
    )

    assert len(instance.run_coordinator.queue()) == 0

    # retries failure
    run = create_run(instance, status=DagsterRunStatus.STARTED, tags={MAX_RETRIES_TAG: "2"})
    dagster_event = DagsterEvent(
        event_type_value=DagsterEventType.PIPELINE_FAILURE.value,
        pipeline_name="foo",
        message="",
    )
    event_record = EventLogEntry(
        user_message="",
        level=logging.ERROR,
        pipeline_name="foo",
        run_id=run.run_id,
        error_info=None,
        timestamp=time.time(),
        dagster_event=dagster_event,
    )
    instance.handle_new_event(event_record)

    list(
        consume_new_runs_for_automatic_reexecution(
            workspace_context,
            instance.get_run_records(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
        )
    )
    assert len(instance.run_coordinator.queue()) == 1

    # doesn't retry again
    list(
        consume_new_runs_for_automatic_reexecution(
            workspace_context,
            instance.get_run_records(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
        )
    )
    assert len(instance.run_coordinator.queue()) == 1

    # retries once the new run failed
    dagster_event = DagsterEvent(
        event_type_value=DagsterEventType.PIPELINE_FAILURE.value,
        pipeline_name="foo",
        message="",
    )
    event_record = EventLogEntry(
        user_message="",
        level=logging.ERROR,
        pipeline_name="foo",
        run_id=instance.run_coordinator.queue()[0].run_id,
        error_info=None,
        timestamp=time.time(),
        dagster_event=dagster_event,
    )
    instance.handle_new_event(event_record)
    list(
        consume_new_runs_for_automatic_reexecution(
            workspace_context,
            instance.get_run_records(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
        )
    )
    assert len(instance.run_coordinator.queue()) == 2

    # doesn't retry a third time
    dagster_event = DagsterEvent(
        event_type_value=DagsterEventType.PIPELINE_FAILURE.value,
        pipeline_name="foo",
        message="",
    )
    event_record = EventLogEntry(
        user_message="",
        level=logging.ERROR,
        pipeline_name="foo",
        run_id=instance.run_coordinator.queue()[1].run_id,
        error_info=None,
        timestamp=time.time(),
        dagster_event=dagster_event,
    )
    instance.handle_new_event(event_record)
    list(
        consume_new_runs_for_automatic_reexecution(
            workspace_context,
            instance.get_run_records(filters=RunsFilter(statuses=[DagsterRunStatus.FAILURE])),
        )
    )
    assert len(instance.run_coordinator.queue()) == 2


def test_daemon_enabled(instance):
    with instance_for_test() as run_retries_disabled_instance:
        assert (
            EventLogConsumerDaemon.daemon_type()
            not in run_retries_disabled_instance.get_required_daemon_types()
        )

    assert EventLogConsumerDaemon.daemon_type() in instance.get_required_daemon_types()


def test_strategy(instance: DagsterInstance):
    run = create_run(
        instance,
        status=DagsterRunStatus.FAILURE,
    )
    assert get_reexecution_strategy(run, instance) is None

    run = create_run(
        instance,
        status=DagsterRunStatus.FAILURE,
        tags={RETRY_STRATEGY_TAG: "FROM_FAILURE"},
    )
    assert get_reexecution_strategy(run, instance) == ReexecutionStrategy.FROM_FAILURE

    run = create_run(
        instance,
        status=DagsterRunStatus.FAILURE,
        tags={RETRY_STRATEGY_TAG: "ALL_STEPS"},
    )
    assert get_reexecution_strategy(run, instance) == ReexecutionStrategy.ALL_STEPS

    run = create_run(
        instance,
        status=DagsterRunStatus.FAILURE,
        tags={RETRY_STRATEGY_TAG: "not a strategy"},
    )
    assert get_reexecution_strategy(run, instance) is None
