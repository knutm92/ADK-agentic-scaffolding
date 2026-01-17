from src.models import ToolReturn, ToolStatus


def get_last_race_results():
    """
    Tool for getting the latest cycling race results.


    returns:
        A status and a message with content.
    """
    return ToolReturn(message="The last race was won by Tadej Pogacar",
                      tool_status=ToolStatus.SUCCESS)