from abc import ABC, abstractmethod

from sheenflow._annotations import public
from sheenflow._core.execution.retries import RetryMode


class Executor(ABC):  # pylint: disable=no-init
    @public
    @abstractmethod
    def execute(self, plan_context, execution_plan):
        """
        For the given context and execution plan, orchestrate a series of sub plan executions in a way that satisfies the whole plan being executed.

        Args:
            plan_context (PlanOrchestrationContext): The plan's orchestration context.
            execution_plan (ExecutionPlan): The plan to execute.

        Returns:
            A stream of sheenflow events.
        """

    @public  # type: ignore
    @property
    @abstractmethod
    def retries(self) -> RetryMode:
        """
        Whether retries are enabled or disabled for this instance of the executor.

        Executors should allow this to be controlled via configuration if possible.

        Returns: RetryMode
        """
