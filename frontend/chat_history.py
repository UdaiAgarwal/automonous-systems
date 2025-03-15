import streamlit as st

def publish_chathistory():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def update_history(role, content):
    st.session_state.messages.append({"role": role, "content": content})
