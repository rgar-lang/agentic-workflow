import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from temporalio.client import Client
from temporal.agent_workflow import AgentWorkflow
import asyncio


async def main():
    from datetime import datetime

    try:
        client = await asyncio.wait_for(Client.connect("localhost:7233"), timeout=10)
    except Exception as exc:
        print(f"Failed to connect to Temporal server: {exc}")
        raise SystemExit(1)

    try:
        result = await asyncio.wait_for(
            client.execute_workflow(
                AgentWorkflow.run,
                id=f"agent-workflow-{datetime.now().timestamp()}",
                task_queue="agent-task-queue"
            ),
            timeout=120
        )
    except asyncio.TimeoutError:
        print("Workflow execution timed out.")
        raise SystemExit(1)
    except Exception as exc:
        print(f"Workflow execution failed: {exc}")
        raise SystemExit(1)

    print(result)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except SystemExit:
        raise
    except Exception as exc:
        print(f"Unhandled error: {exc}")
        raise
