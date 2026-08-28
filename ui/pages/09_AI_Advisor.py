"""
AI Advisor Page - ChatGPT-like interface for agents/conversational_advisor.py.
No business logic - only displays backend responses.
"""

import streamlit as st

st.set_page_config(page_title="AI Advisor - AI Startup Idea Validator", page_icon="🤖", layout="wide", initial_sidebar_state="collapsed")

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.session_state import init_session_state, has_startup_idea
init_session_state()
from components.hero_section import render_page_header, render_startup_info_header
from components.footer import render_footer
from components.chat_ui import render_advisor_page

if not has_startup_idea():
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_page_header("🤖", "AI Startup Advisor", "Chat with your AI advisor about your startup idea", "Home > AI Advisor")
render_startup_info_header()

# ─── Render the full advisor page ───────────────────────────────
render_advisor_page()

render_footer()