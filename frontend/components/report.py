"""
Final Report page for the AI Startup Validator.

Displays the complete final validation report and provides
PDF download using the existing backend PDF endpoint.
"""

import streamlit as st

from components import ui


# ------------------------------------------------------------------
# Safe access helpers
# ------------------------------------------------------------------
def _safe_get(data, key, default=None):
    """Safely get a key from a dict that may be None or missing."""
    if not isinstance(data, dict):
        return default
    return data.get(key, default)


def _safe_list(value):
    """Return a list if value is a list, otherwise an empty list."""
    if isinstance(value, list):
        return value
    return []


def _safe_str(value, default=""):
    """Return a string if value is a string, otherwise default."""
    if isinstance(value, str):
        return value
    return default


def _safe_dict(value):
    """Return a dict if value is a dict, otherwise an empty dict."""
    if isinstance(value, dict):
        return value
    return {}


# ------------------------------------------------------------------
# Render
# ------------------------------------------------------------------
def render_report() -> None:
    """Render the Final Report page."""
    response = st.session_state.validation_response

    if not response:
        st.info("No validation results available yet. Please validate a startup idea first.")
        return

    st.markdown(
        """
        <div class="page-heading">📄 Final Report</div>
        <div class="page-subtitle">
            Review the complete startup validation report.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Show the startup idea
    idea = _safe_get(response, "startup_idea")
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

    # PDF download
    pdf_status = _safe_get(response, "pdf_status")
    pdf_path = _safe_get(pdf_status, "path") if isinstance(pdf_status, dict) else None
    pdf_status_str = _safe_get(pdf_status, "status") if isinstance(pdf_status, dict) else "pending"

    if pdf_status_str == "completed" and pdf_path:
        try:
            import api_client
            pdf_bytes = st.session_state.get("pdf_bytes")
            if pdf_bytes is None:
                pdf_bytes = api_client.download_pdf(pdf_path)
                st.session_state["pdf_bytes"] = pdf_bytes
            st.download_button(
                label="⬇ Download PDF Report",
                data=pdf_bytes,
                file_name="startup_validation_report.pdf",
                mime="application/pdf",
                type="primary",
                use_container_width=True,
            )
        except Exception as exc:
            st.error(f"PDF download failed: {exc}")
    else:
        st.button(
            "⬇ Download PDF Report",
            disabled=True,
            help="PDF is not available for this validation.",
            use_container_width=True,
        )

    st.markdown("---")

    # Full final report
    final_report = _safe_dict(_safe_get(response, "final_report"))
    if not final_report:
        st.info("Final report was not available from the backend.")
    else:
        # Score metrics
        score = _safe_get(final_report, "validation_score")
        potential = _safe_get(final_report, "success_potential")
        recommendation = _safe_get(final_report, "recommendation")

        col1, col2, col3 = st.columns(3)
        with col1:
            ui.render_metric_card(str(score) if score is not None else "—", "Validation Score")
        with col2:
            ui.render_metric_card(_safe_str(potential, "—"), "Success Potential")
        with col3:
            ui.render_metric_card(_safe_str(recommendation, "—"), "Recommendation")

        # Dimension scores
        dimensions = [
            ("Problem Validation", "problem_validation"),
            ("Market Potential", "market_potential"),
            ("Competitive Position", "competitive_position"),
            ("MVP Feasibility", "mvp_feasibility"),
            ("Go-To-Market Readiness", "go_to_market_readiness"),
        ]

        dim_cols = st.columns(len(dimensions))
        for col, (label, key) in zip(dim_cols, dimensions):
            dim = _safe_get(final_report, key)
            if isinstance(dim, dict):
                dim_score = _safe_get(dim, "score")
                with col:
                    ui.render_metric_card(
                        str(dim_score) if dim_score is not None else "—",
                        label,
                    )

        # Assessments
        st.markdown("### Dimension Assessments")
        for label, key in dimensions:
            dim = _safe_get(final_report, key)
            if isinstance(dim, dict):
                assessment = _safe_get(dim, "assessment")
                if assessment:
                    st.markdown(f"**{label}:** {assessment}")

        # Lists
        st.markdown("### Key Findings")
        col1, col2 = st.columns(2)
        with col1:
            ui.render_list(_safe_list(_safe_get(final_report, "key_strengths")), "💪 Key Strengths")
            ui.render_list(_safe_list(_safe_get(final_report, "major_opportunities")), "🚀 Major Opportunities")
            ui.render_list(_safe_list(_safe_get(final_report, "recommended_mvp")), "🛠️ Recommended MVP")
        with col2:
            ui.render_list(_safe_list(_safe_get(final_report, "key_weaknesses")), "⚠️ Key Weaknesses")
            ui.render_list(_safe_list(_safe_get(final_report, "major_risks")), "🔥 Major Risks")
            ui.render_list(_safe_list(_safe_get(final_report, "critical_success_factors")), "✅ Critical Success Factors")

        first_market = _safe_get(final_report, "recommended_first_market")
        if first_market:
            ui.render_card("Recommended First Market", _safe_str(first_market))

        final_assessment = _safe_get(final_report, "final_assessment")
        if final_assessment:
            ui.render_card("Final Assessment", _safe_str(final_assessment))
