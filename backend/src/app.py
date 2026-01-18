from http.client import HTTPException
from loguru import logger
from fastapi import FastAPI
from dotenv import load_dotenv
from src.adk_runtime import AdkRuntime
from src.agents.root.agent import root_agent
from src.models import ChatResponse, ChatRequest
load_dotenv()


app = FastAPI()
runtime = AdkRuntime(agent=root_agent)

@app.get("/")
def get_welcome_message():
    """
    Gets the welcome message at the root endpoint
    """
    return {"message": "Hello from the FastAPI root!"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Sends a message to the agent and retrieves a response.
    """
    try:
        answer = await runtime.generate_response(
            message=request.message,
            session_id=request.session_id
        )

        return ChatResponse(
            response=answer,
            session_id=request.session_id or "fastapi_session"
        )

    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise HTTPException(e)