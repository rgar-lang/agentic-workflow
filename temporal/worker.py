import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from temporal.agent_workflow import AgentWorkflow
from activities.planner_activity import planner_activity
from activities.worker_activity import worker_activity
from activities.reviewer_activity import reviewer_activity
from temporalio.client import Client
from temporalio.worker import Worker

import asyncio


async def main():
    try:
        client = await asyncio.wait_for(Client.connect("localhost:7233"), timeout=10)
    except Exception as exc:
        print(f"Failed to connect to Temporal server: {exc}")
        raise SystemExit(1)

    worker = Worker(
        client,
        task_queue="agent-task-queue",
        workflows=[AgentWorkflow],
        activities=[
            planner_activity,
            worker_activity,
            reviewer_activity
        ]
    )

    print("Temporal Worker Started")

    await worker.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except SystemExit:
        raise
    except Exception as exc:
        print(f"Unhandled error: {exc}")
        raise
