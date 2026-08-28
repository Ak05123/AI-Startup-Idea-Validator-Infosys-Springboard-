"""
Validation Results page for the AI Startup Validator.

Displays the complete validation report returned by the backend.
No nested expanders — all sections use cards, columns, and containers.
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


# ---------------------------------------------------------------------------
# Section renderers
# ---------------------------------------------------------------------------
def render_market_analysis(data):
    """Render the market analysis section."""
    data = _safe_dict(data)
    if not data:
        st.info("Market analysis was not available from the backend.")
        return

    st.markdown("### 📊 Market Analysis")

    target_market = _safe_get(data, "target_market")
    if target_market:
        ui.render_card("Target Market", _safe_str(target_market))

    col1, col2 = st.columns(2)
    with col1:
        ui.render_list(_safe_list(_safe_get(data, "target_customers")), "Target Customers")
        ui.render_list(_safe_list(_safe_get(data, "market_trends")), "Market Trends")
    with col2:
        ui.render_list(_safe_list(_safe_get(data, "market_opportunities")), "Market Opportunities")
        ui.render_list(_safe_list(_safe_get(data, "market_challenges")), "Market Challenges")

    ui.render_list(_safe_list(_safe_get(data, "demand_indicators")), "Demand Indicators")


def render_competitor_analysis(data):
    """Render the competitor analysis section — NO nested expanders."""
    data = _safe_dict(data)
    if not data:
        st.info("Competitor analysis was not available from the backend.")
        return

    st.markdown("### 🏆 Competitor Analysis")

    def render_competitor_list(competitors, title):
        competitors = _safe_list(competitors)
        if not competitors:
            return
        st.markdown(f"**{title}**")
        for comp in competitors:
            if not isinstance(comp, dict):
                continue
            name = _safe_str(_safe_get(comp, "name"), "Competitor")
            desc = _safe_str(_safe_get(comp, "description"))
            strengths = _safe_list(_safe_get(comp, "strengths"))
            weaknesses = _safe_list(_safe_get(comp, "weaknesses"))

            with st.container():
                st.markdown(f"**{name}**")
                if desc:
                    st.markdown(desc)
                if strengths:
                    st.markdown("**Strengths:**")
                    for s in strengths:
                        st.markdown(f"- {s}")
                if weaknesses:
                    st.markdown("**Weaknesses:**")
                    for w in weaknesses:
                        st.markdown(f"- {w}")
                st.markdown("---")

    render_competitor_list(_safe_get(data, "direct_competitors"), "Direct Competitors")
    render_competitor_list(_safe_get(data, "indirect_competitors"), "Indirect Competitors")

    col1, col2 = st.columns(2)
    with col1:
        ui.render_list(_safe_list(_safe_get(data, "competitive_advantages")), "Competitive Advantages")
    with col2:
        ui.render_list(_safe_list(_safe_get(data, "market_gaps")), "Market Gaps")

    ui.render_list(_safe_list(_safe_get(data, "differentiation_opportunities")), "Differentiation Opportunities")


def render_swot_analysis(data):
    """Render the SWOT analysis section."""
    data = _safe_dict(data)
    if not data:
        st.info("SWOT analysis was not available from the backend.")
        return

    st.markdown("### 🧭 SWOT Analysis")

    risk_level = _safe_str(_safe_get(data, "risk_level"))
    if risk_level:
        ui.render_metric_card(risk_level, "Risk Level")

    col1, col2 = st.columns(2)
    with col1:
        ui.render_list(_safe_list(_safe_get(data, "strengths")), "💪 Strengths")
        ui.render_list(_safe_list(_safe_get(data, "opportunities")), "🚀 Opportunities")
    with col2:
        ui.render_list(_safe_list(_safe_get(data, "weaknesses")), "⚠️ Weaknesses")
        ui.render_list(_safe_list(_safe_get(data, "threats")), "🔥 Threats")

    ui.render_list(_safe_list(_safe_get(data, "risk_reasons")), "Risk Reasons")


def render_mvp_analysis(data):
    """Render the MVP analysis section."""
    data = _safe_dict(data)
    if not data:
        st.info("MVP analysis was not available from the backend.")
        return

    st.markdown("### 🛠️ MVP Recommendation")

    problem = _safe_get(data, "problem_statement")
    if problem:
        ui.render_card("Problem Statement", _safe_str(problem))

    value_prop = _safe_get(data, "value_proposition")
    if value_prop:
        ui.render_card("Value Proposition", _safe_str(value_prop))

    col1, col2 = st.columns(2)
    with col1:
        ui.render_list(_safe_list(_safe_get(data, "target_users")), "Target Users")
        ui.render_list(_safe_list(_safe_get(data, "core_features")), "Core Features (v1)")
    with col2:
        ui.render_list(_safe_list(_safe_get(data, "future_features")), "Future Features")
        ui.render_list(_safe_list(_safe_get(data, "success_metrics")), "Success Metrics")

    timeline = _safe_get(data, "estimated_timeline")
    if timeline:
        ui.render_card("Estimated Timeline", _safe_str(timeline))

    tech_stack = _safe_get(data, "recommended_tech_stack")
    if isinstance(tech_stack, dict):
        st.markdown("**Recommended Tech Stack**")
        for key, value in tech_stack.items():
            if isinstance(value, list):
                ui.render_list(value, key.replace("_", " ").title())
            elif value:
                st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")

    phases = _safe_list(_safe_get(data, "development_phases"))
    if phases:
        st.markdown("**Development Phases**")
        for phase in phases:
            if isinstance(phase, dict):
                name = _safe_str(_safe_get(phase, "phase"), "Phase")
                activities = _safe_list(_safe_get(phase, "activities"))
                st.markdown(f"**{name}**")
                for activity in activities:
                    st.markdown(f"- {activity}")
            else:
                st.markdown(f"- {phase}")

    ui.render_list(_safe_list(_safe_get(data, "risks")), "MVP Risks")


def render_gtm_analysis(data):
    """Render the GTM strategy section."""
    data = _safe_dict(data)
    if not data:
        st.info("GTM strategy was not available from the backend.")
        return

    st.markdown("### 📣 Go-To-Market Strategy")

    value_prop = _safe_get(data, "value_proposition")
    if value_prop:
        ui.render_card("Value Proposition", _safe_str(value_prop))

    positioning = _safe_get(data, "positioning_statement")
    if positioning:
        ui.render_card("Positioning Statement", _safe_str(positioning))

    col1, col2 = st.columns(2)
    with col1:
        ui.render_list(_safe_list(_safe_get(data, "marketing_channels")), "Marketing Channels")
        ui.render_list(_safe_list(_safe_get(data, "customer_acquisition_strategy")), "Customer Acquisition")
    with col2:
        ui.render_list(_safe_list(_safe_get(data, "customer_retention_strategy")), "Customer Retention")
        ui.render_list(_safe_list(_safe_get(data, "partnership_opportunities")), "Partnership Opportunities")

    pricing = _safe_get(data, "pricing_strategy")
    if pricing:
        ui.render_card("Pricing Strategy", _safe_str(pricing))

    revenue = _safe_get(data, "revenue_model")
    if revenue:
        ui.render_card("Revenue Model", _safe_str(revenue))

    budget = _safe_get(data, "estimated_budget")
    if budget:
        ui.render_card("Estimated Budget", _safe_str(budget))

    ui.render_list(_safe_list(_safe_get(data, "key_metrics")), "Key Metrics")
    ui.render_list(_safe_list(_safe_get(data, "risks")), "GTM Risks")

    target_audience = _safe_list(_safe_get(data, "target_audience"))
    if target_audience:
        st.markdown("**Target Audience**")
        for segment in target_audience:
            if isinstance(segment, dict):
                name = _safe_str(_safe_get(segment, "segment"), "Segment")
                desc = _safe_str(_safe_get(segment, "description"))
                st.markdown(f"**{name}**")
                if desc:
                    st.markdown(f"- {desc}")

    launch_plan = _safe_list(_safe_get(data, "launch_plan"))
    if launch_plan:
        st.markdown("**Launch Plan**")
        for phase in launch_plan:
            if isinstance(phase, dict):
                name = _safe_str(_safe_get(phase, "phase"), "Phase")
                activities = _safe_list(_safe_get(phase, "activities"))
                st.markdown(f"**{name}**")
                for activity in activities:
                    st.markdown(f"- {activity}")


def render_final_report(data):
    """Render the final validation report."""
    data = _safe_dict(data)
    if not data:
        st.info("Final report was not available from the backend.")
        return

    st.markdown("### 📋 Final Validation Report")

    score = _safe_get(data, "validation_score")
    potential = _safe_get(data, "success_potential")
    recommendation = _safe_get(data, "recommendation")

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
        dim = _safe_get(data, key)
        if isinstance(dim, dict):
            dim_score = _safe_get(dim, "score")
            with col:
                ui.render_metric_card(
                    str(dim_score) if dim_score is not None else "—",
                    label,
                )

    # Assessments
    st.markdown("**Dimension Assessments**")
    for label, key in dimensions:
        dim = _safe_get(data, key)
        if isinstance(dim, dict):
            assessment = _safe_get(dim, "assessment")
            if assessment:
                st.markdown(f"**{label}:** {assessment}")

    # Lists
    col1, col2 = st.columns(2)
    with col1:
        ui.render_list(_safe_list(_safe_get(data, "key_strengths")), "💪 Key Strengths")
        ui.render_list(_safe_list(_safe_get(data, "major_opportunities")), "🚀 Major Opportunities")
        ui.render_list(_safe_list(_safe_get(data, "recommended_mvp")), "🛠️ Recommended MVP")
    with col2:
        ui.render_list(_safe_list(_safe_get(data, "key_weaknesses")), "⚠️ Key Weaknesses")
        ui.render_list(_safe_list(_safe_get(data, "major_risks")), "🔥 Major Risks")
        ui.render_list(_safe_list(_safe_get(data, "critical_success_factors")), "✅ Critical Success Factors")

    first_market = _safe_get(data, "recommended_first_market")
    if first_market:
        ui.render_card("Recommended First Market", _safe_str(first_market))

    final_assessment = _safe_get(data, "final_assessment")
    if final_assessment:
        ui.render_card("Final Assessment", _safe_str(final_assessment))


# ---------------------------------------------------------------------------
# Main results page
# ---------------------------------------------------------------------------
def render_results() -> None:
    """Render the validation results page."""
    response = st.session_state.validation_response

    if not response:
        st.info("No validation results available yet.")
        return

    # Header
    st.markdown(
        """
        <div class="page-heading">✅ Startup Validation Complete</div>
        <div class="page-subtitle">
            Your startup idea has been analyzed by our AI agents.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Startup idea
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

    # Summary metrics from final_report
    final_report = _safe_dict(_safe_get(response, "final_report"))
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

    st.markdown(
        """
        <div class="section-title">Agent Findings</div>
        """,
        unsafe_allow_html=True,
    )

    # Each agent gets its own tab-like section.
    # NOTE: never nest expanders inside these tabs.
    tabs = st.tabs([
        "🔎 Web Search",
        "📊 Market Analysis",
        "🏆 Competitor Analysis",
        "🧭 SWOT & Risk",
        "🛠️ MVP Recommendation",
        "📣 GTM Strategy",
        "📋 Final Report",
    ])

    with tabs[0]:
        _render_web_search_tab(response)
    with tabs[1]:
        render_market_analysis(_safe_get(response, "market_analysis"))
    with tabs[2]:
        render_competitor_analysis(_safe_get(response, "competitor_analysis"))
    with tabs[3]:
        render_swot_analysis(_safe_get(response, "swot_analysis"))
    with tabs[4]:
        render_mvp_analysis(_safe_get(response, "mvp_analysis"))
    with tabs[5]:
        render_gtm_analysis(_safe_get(response, "gtm_analysis"))
    with tabs[6]:
        render_final_report(final_report)


def _render_web_search_tab(response) -> None:
    """Render the Web Search agent findings (research summary / sources)."""
    candidates = [
        _safe_get(response, "web_search_results"),
        _safe_get(response, "web_research"),
        _safe_get(response, "research_summary"),
        _safe_get(response, "search_agent"),
    ]
    web_data = next((c for c in candidates if c), None)

    if isinstance(web_data, dict) and web_data:
        for key, value in web_data.items():
            label = str(key).replace("_", " ").title()
            if isinstance(value, list):
                ui.render_list(value, label)
            elif isinstance(value, str):
                ui.render_card(label, value)
    elif isinstance(web_data, list) and web_data:
        ui.render_list(web_data, "Research Findings")
    else:
        st.info(
            "Web research findings are folded into the other agent sections. "
            "Open the Market or Competitor tabs to see them."
        )
