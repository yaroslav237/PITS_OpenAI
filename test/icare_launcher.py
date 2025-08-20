from conversation_engine import initialize_chatbot, chat_interface
from conversation_engine import load_chat_store
import streamlit as st

chat_store = load_chat_store()
container = st.container()

agent = initialize_chatbot(
    user_name=st.session_state['user_name'],
    study_subject=st.session_state['study_subject'],
    chat_store=chat_store,
    container=container,
    context="Contenu du slide ou résumé du sujet"
)

chat_interface(agent, chat_store, container)
