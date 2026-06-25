from temporalio import activity
from streaming.status_manager import workflow_status
from traces.trace_manager import add_trace
import logging
import asyncio

logger = logging.getLogger(__name__)

@activity.defn
async def worker_activity(worker_name: str):

    workflow_status["current_step"] = worker_name
    workflow_status["status"] = "running"

    add_trace(worker_name, "running")

    logger.info(f"{worker_name} Started")

    await asyncio.sleep(5)

    workflow_status["status"] = "completed"

    add_trace(worker_name, "completed")

    logger.info(f"{worker_name} Completed")

    return {
        "step": worker_name,
        "status": "completed"
    }