"""
AI Startup Validator — Streamlit Frontend
=========================================

Run with:
    streamlit run frontend/streamlit_app.py

This frontend sends startup ideas to the existing FastAPI backend
and displays the real validation results returned by the backend.

The app is a guided workflow controlled by session state:

    home  →  validating  →  results  →  advisor / report

No top navigation — the app controls the user's progression.
"""

import streamlit as st

import config
import api_client
from components import ui
from components.home import render_home
from components.agents import render_agent_workspace
from components.results import render_results
from components.advisor import render_advisor
from components.report import render_report
from utils.styles import inject_css


# ------------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------------
st.set_page_config(
    page_title="AI Startup Validator",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_css()

# ------------------------------------------------------------------
# Session state initialization
# ------------------------------------------------------------------
DEFAULT_INPUTS = {
    "idea": "",
    "country": "",
    "location": "",
    "budget": 0,
    "industry": "TravelTech",
}

for key, value in DEFAULT_INPUTS.items():
    if key not in st.session_state:
        st.session_state[key] = value

if "page" not in st.session_state:
    st.session_state.page = "home"  # home | validating | results | advisor | report

if "validation_status" not in st.session_state:
    st.session_state.validation_status = "idle"  # idle | running | success | error

if "validation_response" not in st.session_state:
    st.session_state.validation_response = None

if "validation_error" not in st.session_state:
    st.session_state.validation_error = None

if "last_submitted" not in st.session_state:
    st.session_state.last_submitted = None


# ------------------------------------------------------------------
# Backend communication
# ------------------------------------------------------------------
def _run_validation():
    """Call the backend and store the result in session state."""
    data = st.session_state.last_submitted
    if not data:
        return

    st.session_state.validation_status = "running"
    st.session_state.validation_error = None
    st.session_state.validation_response = None

    try:
        response = api_client.validate_startup(
            idea=data["idea"],
            country=data["country"],
            location=data["location"],
            budget=str(data["budget"]) if data["budget"] else "",
            industry=data["industry"],
        )
        st.session_state.validation_response = response
        st.session_state.validation_status = "success"
        st.session_state.page = "results"
        st.rerun()
    except api_client.BackendError as exc:
        st.session_state.validation_error = str(exc)
        st.session_state.validation_status = "error"
        st.session_state.page = "home"
        st.rerun()


# ------------------------------------------------------------------
# Main app
# ------------------------------------------------------------------
def main():
    """Main application entry point — state machine."""
    page = st.session_state.page

    if page == "home":
        render_home()
        nav_page = "home"

    elif page == "validating":
        render_agent_workspace()
        # Trigger the backend request on the validating page
        if st.session_state.validation_status == "running":
            _run_validation()
        nav_page = "agents"

    elif page == "results":
        render_results()
        nav_page = "agents"

    elif page == "advisor":
        render_advisor()
        nav_page = "advisor"

    elif page == "report":
        render_report()
        nav_page = "advisor"

    ui.render_bottom_navigation(nav_page)
    ui.render_footer()


if __name__ == "__main__":
    main()