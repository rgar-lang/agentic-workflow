from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    workflow_name: str = "agent-workflow"