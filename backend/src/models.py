from enum import Enum

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