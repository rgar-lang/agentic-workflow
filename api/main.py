from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from streaming.status_stream import event_generator

from workflows.multi_agent_workflow import run_workflow
from streaming.status_manager import workflow_status
from traces.trace_manager import get_traces

app = FastAPI()

@app.get("/stream")
def stream():

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )


@app.get("/")
def home():
    return {
        "message": "Agentic Workflow Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/run")
async def execute_workflow():

    result = await run_workflow()

    return result


@app.get("/status")
def get_status():

    return workflow_status


@app.get("/traces")
def traces():

    return get_traces()