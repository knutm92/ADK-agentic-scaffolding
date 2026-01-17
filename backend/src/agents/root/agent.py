from google.adk.agents import Agent
root_agent = Agent(
    name="root_assistant",
    model="gemini-2.5-flash",
    description="The primary entry point for all user requests.",
    instruction="""
    You are a root agent, which delegates the tasks to sub-agents
    """,
)