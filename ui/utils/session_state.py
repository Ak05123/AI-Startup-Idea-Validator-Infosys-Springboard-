"""
Session State Management for AI Startup Idea Validator.
Centralized initialization and management of all session state variables.
"""

from typing import Any, Dict, List, Optional
import streamlit as st


def init_session_state() -> None:
    """Initialize all required session state variables with defaults."""
    defaults: Dict[str, Any] = {
        # Navigation
        "current_page": "Home",
        "sidebar_selection": "Home",

        # Startup form data
        "startup_idea": "",
        "industry": "",
        "country": "",
        "budget": 0,
        "keywords": [],
        "form_validated": False,

        # Pipeline status
        "pipeline_status": "idle",  # idle | running | completed | error
        "pipeline_progress": 0.0,
        "current_agent": "",
        "agent_timeline": [],

        # Agent results (populated by backend)
        "search_results": None,
        "search_completed": False,
        "market_data": None,
        "market_analysis_done": False,
        "competitor_data": None,
        "competitor_analysis_done": False,
        "swot_data": None,
        "swot_generated": False,
        "mvp_data": None,
        "mvp_generated": False,
        "gtm_data": None,
        "gtm_generated": False,
        "report_data": None,
        "report_generated": False,

        # AI Advisor
        "chat_history": [],
        "advisor_ready": False,

        # Settings
        "settings": {
            "theme": "dark",
            "animations": True,
            "auto_refresh": False,
        },
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def get_form_data() -> Dict[str, Any]:
    """Get all startup form data from session state."""
    return {
        "startup_idea": st.session_state.get("startup_idea", ""),
        "industry": st.session_state.get("industry", ""),
        "country": st.session_state.get("country", ""),
        "budget": st.session_state.get("budget", 0),
        "keywords": st.session_state.get("keywords", []),
    }


def has_startup_idea() -> bool:
    """Check if a startup idea has been submitted."""
    return bool(st.session_state.get("startup_idea", "").strip())


def reset_pipeline() -> None:
    """Reset all pipeline-related session state."""
    st.session_state["pipeline_status"] = "idle"
    st.session_state["pipeline_progress"] = 0.0
    st.session_state["current_agent"] = ""
    st.session_state["agent_timeline"] = []
    st.session_state["search_results"] = None
    st.session_state["search_completed"] = False
    st.session_state["market_data"] = None
    st.session_state["market_analysis_done"] = False
    st.session_state["competitor_data"] = None
    st.session_state["competitor_analysis_done"] = False
    st.session_state["swot_data"] = None
    st.session_state["swot_generated"] = False
    st.session_state["mvp_data"] = None
    st.session_state["mvp_generated"] = False
    st.session_state["gtm_data"] = None
    st.session_state["gtm_generated"] = False
    st.session_state["report_data"] = None
    st.session_state["report_generated"] = False
    st.session_state["chat_history"] = []
    st.session_state["advisor_ready"] = False