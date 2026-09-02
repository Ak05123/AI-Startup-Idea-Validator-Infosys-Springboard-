"""
Home / Landing page for the AI Startup Validator.

A premium, centered AI SaaS landing page with a clean startup
validation form. No navigation chrome — the app controls flow.
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

import config
from config import detect_currency

from components import ui


# ------------------------------------------------------------------
# Industry options
# ------------------------------------------------------------------
INDUSTRY_PLACEHOLDER = "Select Industry"

# ------------------------------------------------------------------
# Minimal bidirectional custom component for live location.
# Asks for browser geolocation ONLY when rendered, resolves it to a
# city/locality via OpenStreetMap (no precise coordinates stored),
# and returns a dict to Python:
#   {"location": "<city>"}   on success
#   {"error": "permission_denied" | "not_supported" | "geocode_failed"}
#   None                     while waiting
# ------------------------------------------------------------------
LOCATION_COMPONENT_DIR = Path(__file__).parent / "location_component"

# NOTE: declare_component() must NOT be called at import time — Streamlit
# registers local components only while a ScriptRunContext exists (i.e.
# during a script run). Declaring at module import causes the component to
# never be registered, and the server returns 404 for its files, which
# surfaces as "Unrecognized component API version: 'undefined'".
_location_component_func = None


def _location_component():
    """Render the geolocation component and return its value (or None)."""
    global _location_component_func
    if _location_component_func is None:
        _location_component_func = components.declare_component(
            "live_location", path=str(LOCATION_COMPONENT_DIR)
        )
    return _location_component_func(key="live_location_widget", height=0)


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
    # One-shot apply of a detected location. This MUST happen before the
    # form widgets are instantiated: a keyed widget ignores the `value=`
    # param once it has rendered, so the widget key itself has to be
    # updated before instantiation for the change to show up.
    apply_loc = st.session_state.pop("live_location_apply", None)
    if apply_loc:
        st.session_state.location = apply_loc
        st.session_state.location_input = apply_loc

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

    # Country sits OUTSIDE the form so that changing it immediately updates
    # the Budget currency label (form widgets only commit on submit).
    col1, col2 = st.columns(2)
    with col1:
        country = st.text_input(
            "Country",
            value=st.session_state.country,
            placeholder="e.g. India",
        )
    with col2:
        # Currency follows the country (India -> INR ₹, USA -> USD $, ...).
        # Empty/unknown country never assumes USD — it asks for one.
        _cur_code, _cur_symbol = detect_currency(country)
        if _cur_code:
            currency_note = f"Currency: **{_cur_code} {_cur_symbol.strip()}**"
        elif country.strip():
            currency_note = "Currency: *unrecognized country*"
        else:
            currency_note = "Currency: *select a country*"
        st.markdown(
            f"""
            <div style="padding-top: 28px; font-size: 0.92rem; opacity: 0.9;">{currency_note}</div>
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

        location = st.text_input(
            "Location",
            value=st.session_state.location,
            placeholder="e.g. Ghaziabad",
            key="location_input",
        )
        fcol1, fcol2 = st.columns(2)
        with fcol1:
            if _cur_code:
                budget_label = f"Budget ({_cur_code} {_cur_symbol.strip()})"
                budget_help = f"Estimated budget for your startup (in {_cur_code})"
            elif country.strip():
                budget_label = "Budget (unrecognized country — please use a known country name)"
                budget_help = "Enter a recognized country above to set the currency"
            else:
                budget_label = "Budget (select a country first)"
                budget_help = "Enter a country above to set the currency"
            budget = st.number_input(
                budget_label,
                min_value=0,
                value=st.session_state.budget,
                step=1000,
                format="%d",
                key="budget_input",
                help=budget_help,
            )
        with fcol2:
            industry = st.selectbox(
                "Industry",
                options=[INDUSTRY_PLACEHOLDER] + INDUSTRIES,
                index=0,
            )

        submitted = st.form_submit_button(
            "🚀 Validate My Startup Idea",
            use_container_width=True,
            type="primary",
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------
    # Live location — only requested when the user explicitly clicks.
    # Uses a minimal bidirectional custom component to get the coords,
    # then reverse-geocodes to city/locality level via OpenStreetMap.
    # Falls back gracefully to manual entry on permission denial.
    # --------------------------------------------------------------
    live_col, info_col = st.columns([1, 3])
    use_live = live_col.button("📍 Use My Current Location", use_container_width=True)

    if use_live:
        st.session_state.live_location_request = True
        st.session_state.live_location_result = None
        st.rerun()

    if st.session_state.get("live_location_request"):
        # Render the geolocation component only while a lookup is active.
        # The browser permission prompt fires ONLY here (never on page load).
        result = _location_component()

        if result is None:
            with info_col:
                st.info("Detecting your location... (allow the browser permission prompt)")
        else:
            # Consume the result and stop rendering the component.
            st.session_state.live_location_request = False
            st.session_state.live_location_result = result
            if isinstance(result, dict) and result.get("location"):
                # Schedule the widget-key update for the top of the next
                # run (see render_home) — writing the widget key here,
                # after it was instantiated this run, would raise
                # StreamlitAPIException.
                st.session_state.live_location_apply = result["location"]
                st.session_state.location = result["location"]
            st.rerun()
    else:
        result = st.session_state.get("live_location_result")
        if isinstance(result, dict) and result:
            if result.get("location"):
                with info_col:
                    st.success(f"Location detected: **{result['location']}**")
            elif result.get("error") == "permission_denied":
                with info_col:
                    st.warning("Location permission was not granted. You can enter your location manually.")
            elif result.get("error") == "not_supported":
                with info_col:
                    st.warning("Live location is not supported by this browser. You can enter your location manually.")
            elif result.get("error"):
                with info_col:
                    st.warning("Could not detect your location automatically. You can enter your location manually.")

    # Show backend error if one occurred
    if st.session_state.validation_status == "error" and st.session_state.validation_error:
        st.error(st.session_state.validation_error)

    # Handle submission
    if submitted:
        if not idea.strip():
            st.error("Please describe your startup idea before validating.")
        elif not industry or industry == INDUSTRY_PLACEHOLDER:
            st.error("Please select an industry.")
        else:
            # Save inputs to session state
            st.session_state.idea = idea.strip()
            st.session_state.country = country.strip()
            st.session_state.location = location.strip()
            st.session_state.budget = int(budget) if budget else 0
            st.session_state.industry = industry
            st.session_state.currency = _cur_code

            # Reset advisor conversation so it never mixes context
            # from a previously validated startup into this one.
            st.session_state.chat_history = []
            st.session_state.pending_question = None

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
                "currency": st.session_state.currency,
            }
            st.rerun()