# 🤖 ADK Agentic Scaffolding

> A production-ready scaffolding for building multi-agent AI systems with Google ADK (Agent Development Kit), featuring a FastAPI backend and Streamlit frontend.

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.123+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Google ADK](https://img.shields.io/badge/Google%20ADK-1.19+-orange.svg)](https://ai.google.dev/adk)

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Development](#-development)
- [License](#-license)

## 🎯 Overview

This project provides a complete scaffolding for building multi-agent AI systems using Google's Agent Development Kit (ADK). It includes:

- **🔧 Backend**: FastAPI-based API server with ADK runtime for agent orchestration
- **💬 Frontend**: Streamlit chat interface for interacting with agents
- **🤝 Multi-Agent System**: Agent architecture in Google ADK framework with delegate capabilities
- **📦 Modern Tooling**: UV package manager for fast dependency management

## ✨ Features

- 🚀 **FastAPI Backend**: High-performance async API with `/chat` endpoint
- 💬 **Streamlit Frontend**: Interactive chat UI with session management
- 🤖 **Multi-Agent Architecture**: Root agent with sub-agent delegation
- 🔄 **Session Management**: Conversation context preservation
- ⚡ **UV Package Manager**: Lightning-fast dependency resolution
- 🛠️ **Extensible Design**: Easy to add new agents and tools

## 📁 Project Structure

```
ADK-agent-scaffolding-cursor/
├── backend/                    # 🚀 FastAPI backend
│   ├── src/
│   │   ├── app.py             # FastAPI application
│   │   ├── adk_runtime.py     # ADK runtime wrapper
│   │   ├── models.py          # Pydantic models
│   │   └── agents/            # Agent definitions
│   │       ├── root/          # Root agent (orchestrator)
│   │       └── cycling_expert/ # Example sub-agent
│   ├── pyproject.toml         # Backend dependencies
│   └── README.md              # Backend documentation
│
├── frontend/                   # 💬 Streamlit frontend
│   ├── src/
│   │   └── streamlit_app.py  # Chat interface
│   ├── pyproject.toml         # Frontend dependencies
│   └── README.md              # Frontend documentation
│
└── README.md                   # This file
```

## 📦 Prerequisites

Before you begin, ensure you have:

- **Python 3.13+** installed
- **UV** package manager installed ([installation guide](https://github.com/astral-sh/uv))
- **Google ADK credentials** configured (see backend README)
- **Environment variables** set up (`.env` file)

## 🚀 Quick Start

### 1️⃣ Clone and Setup

```bash
# Clone the repository (if applicable)
git clone <repository-url>
cd ADK-agent-scaffolding-cursor
```

### 2️⃣ Backend Setup

```bash
cd backend
uv sync                    # Install dependencies
```

Configure your `.env` file with necessary API keys and credentials.

### 3️⃣ Start Backend Server

```bash
# From backend directory
uv run uvicorn src.app:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### 4️⃣ Frontend Setup

```bash
# Open a new terminal
cd frontend
uv sync                    # Install dependencies
```

### 5️⃣ Start Frontend

```bash
# From frontend directory
uv run streamlit run src/streamlit_app.py
```

The Streamlit app will open in your browser at `http://localhost:8501`

## 🏗️ Architecture

### Backend Architecture

```
┌─────────────────┐
│   FastAPI App   │
│   (app.py)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ADK Runtime    │
│ (adk_runtime.py)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Root Agent    │
│  (orchestrator) │
└────────┬────────┘
         │
         ├──► Cycling Expert Agent
         └──► [Other Sub-Agents]
```

### Agent System

- **Root Agent**: Primary entry point that delegates tasks to specialized sub-agents
- **Sub-Agents**: Specialized agents (e.g., `cycling_expert`) that handle domain-specific queries
- **Session Management**: In-memory session service for conversation context

### API Endpoints

- `GET /` - Welcome message
- `POST /chat` - Chat endpoint that accepts messages and returns agent responses

## 💻 Development

### Adding a New Agent

1. Create a new directory under `backend/src/agents/`
2. Define your agent in `agent.py`
3. Register it in the root agent's `sub_agents` list

### Adding Tools

1. Create tool functions in your agent's `tools/` directory
2. Register tools in your agent definition

### Customizing the Frontend

The Streamlit frontend can be customized in `frontend/src/streamlit_app.py`:
- Modify UI components
- Add new features (file uploads, agent selection, etc.)
- Customize styling

## 📚 Documentation

- [Backend README](backend/README.md) - Backend setup and API documentation
- [Frontend README](frontend/README.md) - Frontend setup and usage

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory with:

```env
# Add your Google ADK credentials and API keys here
```

## 🎯 Planned next steps:

- Add commit webhooks to ensure 
- Develop IaC in Terraform and add docker files with the apps
- Introduce static session memory
- Add a remote agent with A2A connection to the backend root agent

## 📝 License

See [LICENSE](LICENSE) file for details.

