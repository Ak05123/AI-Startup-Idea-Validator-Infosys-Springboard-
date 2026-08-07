"""
AI Startup Idea Validator - Main Entry Point
Infosys Springboard Virtual Internship
Premium Enterprise Frontend with Multi-Agent AI Backend Integration

This frontend integrates with:
    app/orchestrator.py - Main pipeline orchestrator
    agents/ - Individual AI agents
    tools/ - Backend tools
    state/ - State management
    prompts/ - AI prompts
    pipeline/ - Pipeline configuration

Architecture:
    UI (Streamlit) → API Client → Backend Orchestrator → AI Agents → Results
"""

import streamlit as st
from pathlib import Path

# ─── Page Configuration ─────────────────────────────────────────
st.set_page_config(
    page_title="AI Startup Idea Validator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Load CSS ───────────────────────────────────────────────────
css_path = Path(__file__).parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ─── Initialize Session State ───────────────────────────────────
from utils.session_state import init_session_state
init_session_state()

# ─── Page Routing ───────────────────────────────────────────────
st.switch_page("pages/01_Home.py")
