from pydantic import BaseModel

class StatusModel(BaseModel):
    current_step: str
    status: str