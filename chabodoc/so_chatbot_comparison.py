import streamlit as st
from pagess.chatbot_comparison import app
st.set_page_config(
    page_title="ChaBoDoc",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None,
)

app()