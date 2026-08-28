"""
Home / Landing page for the AI Startup Validator.

A premium, centered AI SaaS landing page with a clean startup
validation form. No navigation chrome — the app controls flow.
"""

import streamlit as st

from components import ui


# ------------------------------------------------------------------
# Industry options
# ------------------------------------------------------------------
INDUSTRIES = [
    "TravelTech",
    "FinTech",
    "HealthTech",
    "EdTech",
    "E-Commerce",
    "SaaS",
    "AgriTech",
    "PropTech",
    "Logistics",
    "AI / ML",
    "FoodTech",
    "Other",
]


# ------------------------------------------------------------------
# Render
# ------------------------------------------------------------------
def render_home() -> None:
    """Render the centered premium landing page with the validation form."""
    # Vertical centering shell
    st.markdown('<div class="home-shell">', unsafe_allow_html=True)

    # Hero
    st.markdown(
        """
        <span class="hero-badge">AI-Powered Startup Validation</span>
        <div class="hero-title">Validate Your Startup Idea With AI</div>
        <div class="hero-subtitle">
            Turn your idea into a data-driven validation report
            covering market, competition, risks, MVP and GTM.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Form
    with st.form("validation_form", clear_on_submit=False):
        idea = st.text_area(
            "Startup / Idea",
            value=st.session_state.idea,
            placeholder="Describe your startup idea... e.g. AI-powered regional bus booking",
            height=110,
        )

        col1, col2 = st.columns(2)
        with col1:
            country = st.text_input(
                "Country",
                value=st.session_state.country,
                placeholder="e.g. India",
            )
            location = st.text_input(
                "Location",
                value=st.session_state.location,
                placeholder="e.g. Ghaziabad",
            )
        with col2:
            budget = st.number_input(
                "Budget (USD)",
                min_value=0,
                value=st.session_state.budget,
                step=1000,
                format="%d",
                help="Estimated budget for your startup",
            )
            industry = st.selectbox(
                "Industry",
                options=INDUSTRIES,
                index=INDUSTRIES.index(st.session_state.industry)
                if st.session_state.industry in INDUSTRIES
                else 0,
            )

        submitted = st.form_submit_button(
            "🚀 Validate My Startup Idea",
            use_container_width=True,
            type="primary",
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # Show backend error if one occurred
    if st.session_state.validation_status == "error" and st.session_state.validation_error:
        st.error(st.session_state.validation_error)

    # Handle submission
    if submitted:
        if not idea.strip():
            st.error("Please describe your startup idea before validating.")
        else:
            # Save inputs to session state
            st.session_state.idea = idea.strip()
            st.session_state.country = country.strip()
            st.session_state.location = location.strip()
            st.session_state.budget = int(budget) if budget else 0
            st.session_state.industry = industry

            # Transition to the validating screen
            st.session_state.page = "validating"
            st.session_state.validation_status = "running"
            st.session_state.validation_response = None
            st.session_state.validation_error = None
            st.session_state.last_submitted = {
                "idea": st.session_state.idea,
                "country": st.session_state.country,
                "location": st.session_state.location,
                "budget": st.session_state.budget,
                "industry": st.session_state.industry,
            }
            st.rerun()