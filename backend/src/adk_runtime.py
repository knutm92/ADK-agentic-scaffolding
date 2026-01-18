from typing import Optional

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.genai.types import Content, Part
from google.adk.sessions import InMemorySessionService, DatabaseSessionService
from loguru import logger
class AdkRuntime:
    """
    Basic runtime for ADK agents
    """
    def __init__(self, agent: Agent):
        self.agent = agent
        self.session_service = InMemorySessionService()
        logger.info("Initializing ADK Runtime...")
        self.runner = Runner(
            agent = self.agent,
            app_name=self.agent.name,
            session_service=self.session_service,
        )
        logger.info("ADK Runtime initialized successfully!")

    async def generate_response(self,
                                message: str,
                                session_id: Optional[str] = "fastapi_cid"):
        agent_output=""
        user_id = "fastapi"
        new_message=Content(role="user", parts=[Part(text=message)])

        # Checks if the session exists and create a new one if no existing is matched with session_id
        session = await self.session_service.get_session(
            app_name = self.agent.name,
            user_id=user_id,
            session_id=session_id
        )
        if not session:
            logger.info("Starting a new conversation session...")
            await self.session_service.create_session(
                app_name=self.agent.name,
                user_id=user_id,
                session_id=session_id
            )

        async for event in self.runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=new_message
        ):
            # Streaming
            if hasattr(event, "delta") and getattr(event.delta, "text", None):
                agent_output += event.delta.text
                continue

            if hasattr(event, "content_block") and getattr(event.content_block, "text", None):
                agent_output += event.content_block.text

            if hasattr(event, "content") and event.content and event.content.parts:
                for part in event.content.parts:
                    if getattr(part, "text", None):
                        agent_output += part.text

            # No streaming
            # if event.is_final_response():
            #     # Extract text from the first part of the content
            #     if event.content and event.content.parts:
            #         return event.content.parts[0].text
        return agent_output