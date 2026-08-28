"""
Reusable UI components for the AI Startup Validator frontend.

These helpers keep the page modules clean and provide a consistent,
professional look across the app.
"""

import streamlit as st


# ------------------------------------------------------------------
# Cards
# ------------------------------------------------------------------
def render_card(title: str, body: str) -> None:
    """Render a simple card with a title and body text."""
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-body">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric_card(value: str, label: str) -> None:
    """Render a metric-style card."""
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------
# Action cards
# ------------------------------------------------------------------
def render_action_card(icon: str, title: str, description: str) -> None:
    """Render a clickable action card."""
    st.markdown(
        f"""
        <div class="action-card">
            <div class="action-card-icon">{icon}</div>
            <div class="action-card-title">{title}</div>
            <div class="action-card-desc">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------
# Status pills
# ------------------------------------------------------------------
def render_status_pill(status: str) -> str:
    """Return an HTML status pill for a given status string."""
    status = (status or "waiting").lower()
    css_class = f"status-{status}"
    if css_class not in {
        "status-completed",
        "status-failed",
        "status-running",
        "status-waiting",
    }:
        css_class = "status-waiting"
        status = "waiting"

    label = status.capitalize()
    dot = ""
    if status == "running":
        dot = '<span class="pulse-dot"></span>'
    elif status == "completed":
        dot = "✓"
    elif status == "failed":
        dot = "✗"

    return (
        f'<span class="status-pill {css_class}">{dot} {label}</span>'
    )


# ------------------------------------------------------------------
# Agent cards
# ------------------------------------------------------------------
def render_agent_card(
    icon: str,
    name: str,
    description: str,
    status: str = "waiting",
) -> None:
    """Render a single agent card with a status pill."""
    st.markdown(
        f"""
        <div class="agent-card">
            <div class="agent-icon">{icon}</div>
            <div class="agent-info">
                <div class="agent-name">{name}</div>
                <div class="agent-desc">{description}</div>
            </div>
            <div class="agent-status">
                {render_status_pill(status)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------
# List rendering helpers
# ------------------------------------------------------------------
def render_list(items, title: str | None = None) -> None:
    """Render a list of items as bullet points, safely."""
    if not items:
        return
    if title:
        st.markdown(f"**{title}**")
    for item in items:
        st.markdown(f"- {item}")


def render_key_value_pairs(data: dict) -> None:
    """Render a dict of key/value pairs as a simple list."""
    for key, value in data.items():
        st.markdown(f"**{key}:** {value}")


# ------------------------------------------------------------------
# Bottom navigation
# ------------------------------------------------------------------
def render_bottom_navigation(current_page: str) -> None:
    """Render the bottom navigation bar with page-appropriate buttons."""
    st.markdown("---")

    if current_page == "home":
        # [🏠 Home] [🤖 Agents]
        col1, col2 = st.columns(2)
        with col1:
            st.button("🏠 Home", use_container_width=True, key="nav_home", disabled=True)
        with col2:
            if st.button("🤖 Agents", use_container_width=True, key="nav_agents"):
                st.session_state.page = "results"
                st.rerun()

    elif current_page == "agents":
        # [🏠 Home] [🤖 Agents] [🤖 AI Advisor]
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🏠 Home", use_container_width=True, key="nav_home"):
                st.session_state.page = "home"
                st.rerun()
        with col2:
            st.button("🤖 Agents", use_container_width=True, key="nav_agents", disabled=True)
        with col3:
            if st.button("🤖 AI Advisor", use_container_width=True, key="nav_advisor"):
                st.session_state.page = "advisor"
                st.rerun()

    elif current_page == "advisor":
        # [🏠 Home] [🤖 Agents] [🤖 AI Advisor] [📄 Download PDF]
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("🏠 Home", use_container_width=True, key="nav_home"):
                st.session_state.page = "home"
                st.rerun()
        with col2:
            if st.button("🤖 Agents", use_container_width=True, key="nav_agents"):
                st.session_state.page = "results"
                st.rerun()
        with col3:
            st.button("🤖 AI Advisor", use_container_width=True, key="nav_advisor", disabled=True)
        with col4:
            _render_pdf_download_button()


def _render_pdf_download_button() -> None:
    """Render the PDF download button using the existing backend functionality."""
    response = st.session_state.get("validation_response")
    if not response or not isinstance(response, dict):
        st.button(
            "📄 Download PDF",
            disabled=True,
            help="No validation results available.",
            key="nav_pdf_disabled",
            use_container_width=True,
        )
        return

    pdf_status = response.get("pdf_status")
    pdf_path = pdf_status.get("path") if isinstance(pdf_status, dict) else None
    pdf_status_str = pdf_status.get("status") if isinstance(pdf_status, dict) else "pending"

    if pdf_status_str == "completed" and pdf_path:
        try:
            import api_client
            pdf_bytes = st.session_state.get("pdf_bytes")
            if pdf_bytes is None:
                pdf_bytes = api_client.download_pdf(pdf_path)
                st.session_state["pdf_bytes"] = pdf_bytes
            st.download_button(
                label="📄 Download PDF",
                data=pdf_bytes,
                file_name="startup_validation_report.pdf",
                mime="application/pdf",
                key="nav_download_pdf",
                use_container_width=True,
            )
        except Exception as exc:
            st.error(f"PDF download failed: {exc}")
    else:
        st.button(
            "📄 Download PDF",
            disabled=True,
            help="PDF is not available for this validation.",
            key="nav_pdf_disabled",
            use_container_width=True,
        )


# ------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------
def render_footer() -> None:
    """Render the app footer."""
    st.markdown(
        """
        <div class="footer">
            AI Startup Validator &nbsp;•&nbsp; Powered by Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )