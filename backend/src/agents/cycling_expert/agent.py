from google.adk.agents import Agent

from src.agents.cycling_expert.tools.cycling import get_last_race_results

cycling_expert = Agent(
    name="cycling_expert",
    model="gemini-2.5-flash",
    description="The agent with expert knowledge on cycling.",
    instruction="""
    You are a cycling expert agent, who acts as a training and general bike advisor.
    If a user wants to learn the results of the last cycling race results, use `get_last_race_results` tool.
    """,
    tools=[get_last_race_results]
)