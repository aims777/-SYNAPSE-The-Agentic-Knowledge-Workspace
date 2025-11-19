import streamlit as st
import requests
import json

def sidebar():
    with st.sidebar:
        st.header("📚 Document Upload")
        uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
        if uploaded_file is not None:
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            try:
                response = requests.post("http://localhost:8000/upload", files=files)
                if response.status_code == 200:
                    st.success(f"Successfully uploaded {uploaded_file.name}")
                else:
                    st.error(f"Error uploading file: {response.text}")
            except requests.exceptions.ConnectionError as e:
                st.error(f"Connection error: {e}")

        st.divider()

        st.header("⚙️ Model Settings")
        st.selectbox("LLM Model", ["llama3-70b-8192", "mixtral-8x7b-32768"], key="llm_model")
        st.slider("Temperature", 0.0, 1.0, 0.7, 0.1, key="temperature")

        st.divider()

        st.header("🔄 Session Control")
        if st.button("New Chat"):
            st.session_state.messages = []
            st.session_state.analytics = {}
            st.experimental_rerun()

        if st.button("Export Chat"):
            chat_json = json.dumps(st.session_state.messages, indent=2)
            st.download_button(
                label="Download Chat (JSON)",
                data=chat_json,
                file_name="chat_history.json",
                mime="application/json",
            )
