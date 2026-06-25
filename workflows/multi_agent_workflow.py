from traces.trace_manager import clear_traces
from streaming.status_manager import workflow_status

from activities.planner_activity import planner_activity
from activities.worker_activity import worker_activity
from activities.reviewer_activity import reviewer_activity

import asyncio


async def run_workflow():

    clear_traces()

    print("Workflow Started")

    planner_result = await planner_activity()

    # Run two workers in parallel
    worker1_result, worker2_result = await asyncio.gather(
    worker_activity("worker-1"),
    worker_activity("worker-2")
)

    reviewer_result = await reviewer_activity()

    workflow_status["current_step"] = "completed"
    workflow_status["status"] = "completed"

    return {
        "planner": planner_result,
        "worker1": worker1_result,
        "worker2": worker2_result,
        "reviewer": reviewer_result,
        "workflow_status": "completed"
    }