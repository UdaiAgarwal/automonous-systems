import streamlit as st
from middleware.main_llms import invoke_llm
from frontend.sidebar import sidebar
from frontend.chat_history import publish_chathistory, update_history

# ============ frontend ======================
st.set_page_config(layout = "wide")
# Header
st.title("Echo Bot")
# sidebar
sidebar()

# ============= chat bot stuff here ================
publish_chathistory() # show chat history from session history


# React to user input
if prompt := st.chat_input("Ask anything!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    

    response = f"Echo: {prompt}"
    response = invoke_llm(prompt, st.session_state["model"])
    # Display assistant response in chat message container
    st.chat_message("assistant").markdown(response)

    # ============= adding to history =======================
    update_history("user", prompt)
    update_history("assistant", response)