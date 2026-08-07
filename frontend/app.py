"""
AI Startup Idea Validator - Main Entry Point
Infosys Springboard Virtual Internship
"""
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="AI Startup Idea Validator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load CSS
css_path = Path(__file__).parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Import utilities
from utils.helpers import init_session_state
init_session_state()

# Route to Home page
st.switch_page("pages/01_Home.py")