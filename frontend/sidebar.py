import streamlit as st

def sidebar():
    side = st.sidebar
    with side:
        
        models = ["meta-llama/Meta-Llama-3-8B-Instruct"]
        model = st.selectbox("Model", models)
        st.session_state["model"] = model