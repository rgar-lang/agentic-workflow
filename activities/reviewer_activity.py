from temporalio import activity
from streaming.status_manager import workflow_status
from traces.trace_manager import add_trace
import logging
import asyncio

logger = logging.getLogger(__name__)


@activity.defn
async def reviewer_activity():

    workflow_status["current_step"] = "reviewer"
    workflow_status["status"] = "running"

    add_trace("reviewer", "running")

    logger.info("Reviewer Started")

    await asyncio.sleep(5)

    workflow_status["status"] = "completed"

    add_trace("reviewer", "completed")

    logger.info("Reviewer Completed")

    return {
        "step": "reviewer",
        "status": "completed"
    }