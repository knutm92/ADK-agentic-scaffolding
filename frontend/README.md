# Streamlit Frontend

A simple Streamlit frontend for chatting with ADK agents via the FastAPI `/chat` endpoint.

## Setup

1. Install dependencies using uv:
```bash
uv sync
```

## Running

1. Start FastAPI server:
```bash
uv run uvicorn app:app --reload --port 8080
```


2. Start the Streamlit app:
```bash
uv run streamlit run app.py --server.port 8081
```

3. The app will open in your browser. You can:
   - Chat with your agent
   - Start a new session
   - Clear chat history
   - Configure the API base URL in the sidebar
