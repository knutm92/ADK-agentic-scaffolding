from enum import Enum
from typing import Optional

from pydantic import BaseModel

class ToolStatus(str, Enum):
    """
    Constants with tool status values
    """
    SUCCESS: str = "success"
    ERROR: str = "error"

class ToolReturn(BaseModel):
    tool_status: ToolStatus
    message: str

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: Optional[str]