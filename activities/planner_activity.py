from temporalio import activity
from streaming.status_manager import workflow_status
from traces.trace_manager import add_trace
import logging
import asyncio

logger = logging.getLogger(__name__)


@activity.defn
async def planner_activity():

    workflow_status["current_step"] = "planner"
    workflow_status["status"] = "running"

    add_trace("planner", "running")

    logger.info("Planner Started")

    await asyncio.sleep(5)

    workflow_status["status"] = "completed"

    add_trace("planner", "completed")

    logger.info("Planner Completed")

    return {
        "step": "planner",
        "status": "completed"
    }