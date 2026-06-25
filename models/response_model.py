from pydantic import BaseModel

class WorkflowResponse(BaseModel):
    planner: dict
    worker1: dict
    worker2: dict
    reviewer: dict