from pydantic import BaseModel

class TraceModel(BaseModel):
    step: str
    status: str
    timestamp: str