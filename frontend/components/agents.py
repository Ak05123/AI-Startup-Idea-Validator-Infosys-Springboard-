"""
Validation Progress screen for the AI Startup Validator.

Shows a clean "Validation in progress" state while the backend
request is running, then automatically transitions to results.
"""

import streamlit as st

from components import ui


# ------------------------------------------------------------------
# Agent definitions (UI representations of the existing backend agents)
# ------------------------------------------------------------------
AGENTS = [
    {
        "icon": "🔎",
        "name": "Web Search Agent",
        "description": "Researching market and startup information",
    },
    {
        "icon": "📊",
        "name": "Market Analysis Agent",
        "description": "Evaluating market opportunity and demand",
    },
    {
        "icon": "🏆",
        "name": "Competitor Analysis Agent",
        "description": "Analyzing competitors and differentiation",
    },
    {
        "icon": "🧩",
        "name": "SWOT & Risk Agent",
        "description": "Identifying strengths, weaknesses, opportunities and threats",
    },
    {
        "icon": "🚀",
        "name": "MVP Recommendation Agent",
        "description": "Determining core MVP features",
    },
    {
        "icon": "📣",
        "name": "GTM Strategy Agent",
        "description": "Building the go-to-market strategy",
    },
    {
        "icon": "📄",
        "name": "Report Generation Agent",
        "description": "Preparing the final validation report",
    },
]


# ------------------------------------------------------------------
# Render
# ------------------------------------------------------------------
def render_agent_workspace() -> None:
    """Render the validation progress screen."""
    st.markdown(
        """
        <div class="page-heading">🤖 AI Agents at Work</div>
        <div class="page-subtitle">
            Our AI agents are analyzing your startup idea from
            multiple business perspectives.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Show the submitted idea
    idea = st.session_state.last_submitted.get("idea", "") if st.session_state.last_submitted else ""
    if idea:
        st.markdown(
            f"""
            <div class="idea-card">
                <div class="idea-label">Startup Idea</div>
                <div class="idea-text">"{idea}"</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # All agents are "running" while the backend request is in flight
    for agent in AGENTS:
        ui.render_agent_card(
            icon=agent["icon"],
            name=agent["name"],
            description=agent["description"],
            status="running",
        )

    # Professional loading state while the API request runs
    with st.spinner("Running the AI validation pipeline..."):
        st.markdown(
            """
            <div style="color:#94a3b8;font-size:0.9rem;line-height:1.8;text-align:center;">
                Analyzing market, competitors, risks, MVP and go-to-market strategy...
            </div>
            """,
            unsafe_allow_html=True,
        )