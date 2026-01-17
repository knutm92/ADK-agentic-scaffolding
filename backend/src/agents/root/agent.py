from google.adk.agents import Agent

from src.agents.cycling_expert.agent import cycling_expert

root_agent = Agent(
    name="root_assistant",
    model="gemini-2.5-flash",
    description="The primary entry point for all user requests.",
    instruction="""
    You are a root agent, which delegates the tasks to sub-agents.
    
    Available agents:
    `cycling_expert`: Assists with cycling-related questions.
    """,
    tools=[],
    sub_agents=[cycling_expert]
)