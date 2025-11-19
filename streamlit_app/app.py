import streamlit as st
import requests
import json

from components.sidebar import sidebar
from components.chat_box import chat_box
from components.analytics_card import analytics_card

# Page configuration
st.set_page_config(
    page_title="Synapse - The Agentic Knowledge Workspace",
    page_icon="⭐",
    layout="wide",
)

# Load styles
with open("styles.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "analytics" not in st.session_state:
    st.session_state.analytics = {}

# Sidebar
sidebar()

# Main content
st.title("⭐ SYNAPSE – The Agentic Knowledge Workspace")

# Chat interface
chat_box()

# Analytics panel
if st.session_state.analytics:
    analytics_card(st.session_state.analytics)

# Handle chat input
if prompt := st.chat_input("Ask a question about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            with requests.post("http://localhost:8000/query", params={"question": prompt}, stream=True) as r:
                for chunk in r.iter_content(chunk_size=None):
                    if chunk:
                        full_response += chunk.decode('utf-8')
                        message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            # For demonstration, we'll just show the final answer as analytics.
            # In a real application, you would parse the agent's output to get insights, summary, etc.
            st.session_state.analytics = {
                "insights": ["This is a key insight."],
                "entities": ["Entity 1", "Entity 2"],
                "summary": "This is a summary of the response.",
                "sources": ["Source 1", "Source 2"],
            }
            st.experimental_rerun()
        except requests.exceptions.ConnectionError as e:
            st.error(f"Connection error: {e}")
