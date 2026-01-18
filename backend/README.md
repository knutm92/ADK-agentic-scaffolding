# ADK Backend

FastAPI backend for multi-agent AI systems powered by Google ADK (Agent Development Kit).

## Setup

1. Install dependencies using uv:
```bash
uv sync
```

Or if you want to install in your current environment:
```bash
uv pip install -e .
```

2. Create a `.env` file with your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

## Running

Start the FastAPI server:
```bash
uv run uvicorn src.app:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Welcome message
- `POST /chat` - Chat endpoint that accepts messages and returns agent responses

Example request:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "session_id": "my-session"}'
```