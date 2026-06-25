from datetime import timedelta
import asyncio

from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from activities.planner_activity import planner_activity
    from activities.worker_activity import worker_activity
    from activities.reviewer_activity import reviewer_activity


@workflow.defn
class AgentWorkflow:

    @workflow.run
    async def run(self):

        # Planner
        planner_result = await workflow.execute_activity(
            planner_activity,
            start_to_close_timeout=timedelta(seconds=20),
            schedule_to_close_timeout=timedelta(seconds=30),
            retry_policy=RetryPolicy(maximum_attempts=3),
        )

        # Parallel Workers
        worker_result_1, worker_result_2 = await asyncio.gather(

    workflow.execute_activity(
        worker_activity,
        "worker-1",
        start_to_close_timeout=timedelta(seconds=20),
        schedule_to_close_timeout=timedelta(seconds=30),
        retry_policy=RetryPolicy(maximum_attempts=3),
    ),

    workflow.execute_activity(
        worker_activity,
        "worker-2",
        start_to_close_timeout=timedelta(seconds=20),
        schedule_to_close_timeout=timedelta(seconds=30),
        retry_policy=RetryPolicy(maximum_attempts=3),
    ),
)

        # Reviewer
        reviewer_result = await workflow.execute_activity(
            reviewer_activity,
            start_to_close_timeout=timedelta(seconds=20),
            schedule_to_close_timeout=timedelta(seconds=30),
            retry_policy=RetryPolicy(maximum_attempts=3),
        )

        return {
            "planner": planner_result,
            "worker1": worker_result_1,
            "worker2": worker_result_2,
            "reviewer": reviewer_result,
        }