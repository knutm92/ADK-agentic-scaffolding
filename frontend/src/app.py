import streamlit as st
import requests
from typing import Optional
import uuid

# Configuration
API_BASE_URL = st.sidebar.text_input(
    "API Base URL",
    value="http://localhost:8080",
    help="The base URL of FastAPI backend"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "api_available" not in st.session_state:
    st.session_state.api_available = True


def send_message(message: str, session_id: str) -> Optional[str]:
    """
    Send a message to the FastAPI /chat endpoint and return the response.
    """
    try:
        response = requests.post(
            f"{API_BASE_URL}/chat",
            json={
                "message": message,
                "session_id": session_id
            },
            timeout=60  # 60 second timeout for agent responses
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response received")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {e}")
        return None


# Page configuration
st.set_page_config(
    page_title="Agent Chat",
    page_icon="💬",
    layout="wide"
)

# Title
st.title("💬 Agent Chat Interface")
st.caption(f"Session ID: {st.session_state.session_id}")

# Sidebar
with st.sidebar:
    st.header("Settings")

    if st.button("🔄 New Session"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.markdown("### Chat History")
    st.info(f"{len(st.session_state.messages)} messages in this session")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = send_message(prompt, st.session_state.session_id)

            if response:
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                error_msg = "Sorry, I couldn't connect to the agent. Please check that the FastAPI backend is running."
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Footer
st.divider()
st.caption("💡 Make sure your FastAPI backend is running on the configured URL")