"""Final Report - Displays results from the backend report_agent.py."""
import streamlit as st
import json
from pathlib import Path
st.set_page_config(page_title="Final Report", page_icon="📄", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()
from utils.page_utils import render_breadcrumb, render_section, render_page_footer, navigate_to
from utils.backend_client import parse_json_response

startup_idea = st.session_state.get("startup_idea", "")
industry = st.session_state.get("industry", "")
country = st.session_state.get("country", "")
budget = st.session_state.get("budget", 0)
keywords = st.session_state.get("keywords", [])

if not startup_idea:
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_breadcrumb("📄 Final Report")

# Get backend response
backend_response = st.session_state.get("backend_response")
if not backend_response:
    st.warning("⚠️ No analysis results found. Please run the validation from the Web Search page first.")
    if st.button("🌐 Go to Web Search", use_container_width=True):
        navigate_to("02_Web_Search_Agent.py")
    st.stop()

# Parse report from backend
report_raw = backend_response.get("report", "{}")
report = parse_json_response(report_raw)

# Report Header
st.markdown(f"""
<div style="text-align:center;padding:2.5rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;margin-bottom:1.5rem;">
    <div style="font-size:3rem;margin-bottom:0.75rem;">📄</div>
    <div style="font-size:1.5rem;font-weight:800;background:linear-gradient(135deg,#fff,#4d94ff,#00d4aa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">AI Startup Idea Validator</div>
    <div style="font-size:1.1rem;font-weight:600;color:#4d94ff;margin-top:0.5rem;">Startup Idea</div>
    <div style="font-size:0.9rem;color:rgba(255,255,255,0.5);margin-top:0.25rem;">{industry or "N/A"} | {country or "N/A"}</div>
</div>
""", unsafe_allow_html=True)

if report.get("raw") is not None:
    st.info("Report data is not available in structured format.")
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">{report.get("raw", "")}</div>', unsafe_allow_html=True)
else:
    # Executive Summary
    render_section("📋 Executive Summary")
    st.markdown(f"""
    <div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;">
    <p>This report presents a comprehensive validation analysis for your startup idea in the <strong>{industry or 'target'}</strong> industry.</p>
    <p><strong>Startup Idea:</strong> {startup_idea}</p>
    <p><strong>Final Verdict:</strong> <span style="color:#00d4aa;font-weight:700;">{report.get("final_verdict", "N/A")}</span></p>
    <p><strong>Risk Level:</strong> <span style="color:#ffd93d;font-weight:700;">{report.get("risk_level", "N/A")}</span></p>
    </div>
    """, unsafe_allow_html=True)

    # Scores
    render_section("📊 Validation Scores")
    scorecard = report.get("scorecard", {})
    overall_score = report.get("overall_validation_score", 0)
    confidence = report.get("validation_confidence", 0)
    viability = report.get("viability_estimate_percent", 0)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(77,148,255,0.3);border-radius:12px;"><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Overall Score</div><div style="font-size:2rem;font-weight:700;color:#4d94ff;margin:0.25rem 0;">{overall_score}/100</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Weighted validation</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(0,212,170,0.3);border-radius:12px;"><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Confidence</div><div style="font-size:2rem;font-weight:700;color:#00d4aa;margin:0.25rem 0;">{confidence}%</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Research confidence</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,217,61,0.3);border-radius:12px;"><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Viability</div><div style="font-size:2rem;font-weight:700;color:#ffd93d;margin:0.25rem 0;">{viability}%</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Model-based estimate</div></div>', unsafe_allow_html=True)
    with col4:
        risk_color = "#00d4aa" if report.get("risk_level") == "Low" else "#ffd93d" if report.get("risk_level") == "Medium" else "#ff6b6b"
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid {risk_color}33;border-radius:12px;"><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Risk Level</div><div style="font-size:1.5rem;font-weight:700;color:{risk_color};margin:0.25rem 0;">{report.get("risk_level", "N/A")}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Overall risk</div></div>', unsafe_allow_html=True)

    # Scorecard Details
    if scorecard:
        render_section("📊 Scorecard Breakdown", "Detailed scoring by category")
        score_items = [
            ("Market Demand", scorecard.get("market_demand", {}), "#4d94ff"),
            ("Competitive Position", scorecard.get("competitive_position", {}), "#00d4aa"),
            ("Problem Solution Fit", scorecard.get("problem_solution_fit", {}), "#ffd93d"),
            ("MVP Feasibility", scorecard.get("mvp_feasibility", {}), "#ff6b6b"),
            ("Differentiation", scorecard.get("differentiation", {}), "#4d94ff"),
            ("GTM Readiness", scorecard.get("gtm_readiness", {}), "#00d4aa"),
            ("Risk Management", scorecard.get("risk_management", {}), "#ffd93d"),
        ]
        for title, data, color in score_items:
            score = data.get("score", 0) if isinstance(data, dict) else 0
            reason = data.get("reason", "") if isinstance(data, dict) else ""
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;"><span style="font-weight:600;font-size:0.9rem;">{title}</span><span style="font-size:1.1rem;font-weight:700;color:{color};">{score}/100</span></div><div style="width:100%;height:6px;background:rgba(255,255,255,0.1);border-radius:3px;"><div style="width:{score}%;height:100%;background:{color};border-radius:3px;"></div></div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);margin-top:0.5rem;">{reason}</div></div>', unsafe_allow_html=True)

    # Strongest Factors
    strongest = report.get("strongest_factors", [])
    if strongest:
        render_section("💪 Strongest Factors", "Key strengths identified")
        for factor in strongest:
            st.markdown(f'<div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">💪</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{factor}</span></div>', unsafe_allow_html=True)

    # Weakest Factors
    weakest = report.get("weakest_factors", [])
    if weakest:
        render_section("⚠️ Weakest Factors", "Areas needing improvement")
        for factor in weakest:
            st.markdown(f'<div style="background:rgba(255,107,107,0.05);border:1px solid rgba(255,107,107,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">⚠️</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{factor}</span></div>', unsafe_allow_html=True)

    # Key Risks
    key_risks = report.get("key_risks", [])
    if key_risks:
        render_section("🔥 Key Risks", "Critical risks to address")
        for risk in key_risks:
            st.markdown(f'<div style="background:rgba(255,217,61,0.05);border:1px solid rgba(255,217,61,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">🔥</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{risk}</span></div>', unsafe_allow_html=True)

    # Next Actions
    next_actions = report.get("next_actions", [])
    if next_actions:
        render_section("✅ Next Actions", "Recommended next steps")
        for i, action in enumerate(next_actions):
            st.markdown(f'<div style="background:rgba(77,148,255,0.05);border:1px solid rgba(77,148,255,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;color:#4d94ff;font-weight:700;">{i + 1}</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{action}</span></div>', unsafe_allow_html=True)

    # Final Verdict
    render_section("🎯 Final Verdict")
    verdict = report.get("final_verdict", "N/A")
    verdict_color = "#00d4aa" if verdict in ["Strong Go", "Go"] else "#ffd93d" if verdict == "Proceed with Caution" else "#ff6b6b"
    st.markdown(f'<div style="background:rgba(0,212,170,0.05);border:1px solid {verdict_color}44;border-radius:16px;padding:1.5rem;margin:1rem 0;text-align:center;"><div style="font-size:2rem;margin-bottom:0.5rem;">🎯</div><div style="font-size:1.5rem;font-weight:800;color:{verdict_color};">{verdict}</div><div style="font-size:0.9rem;color:rgba(255,255,255,0.5);margin-top:0.5rem;">Based on comprehensive multi-agent analysis</div></div>', unsafe_allow_html=True)

# Export
render_section("📤 Export Report")
report_data = {
    "startup_idea": startup_idea,
    "industry": industry,
    "country": country,
    "budget": budget,
    "keywords": keywords,
    "report": report,
    "competitors": backend_response.get("competitors", []),
    "market_analysis": backend_response.get("market_analysis", ""),
    "swot_analysis": backend_response.get("swot_analysis", ""),
    "mvp_recommendation": backend_response.get("mvp_recommendation", ""),
    "gtm_strategy": backend_response.get("gtm_strategy", ""),
}
col1, col2, col3 = st.columns(3)
with col1:
    st.download_button("📥 Download JSON", data=json.dumps(report_data, indent=2, default=str), file_name="startup_validation_report.json", mime="application/json", use_container_width=True)
with col2:
    md_content = f"""# Startup Validation Report

## Startup Idea
{startup_idea}

## Industry
{industry or 'N/A'}

## Final Verdict
{report.get('final_verdict', 'N/A')}

## Risk Level
{report.get('risk_level', 'N/A')}

## Overall Score
{report.get('overall_validation_score', 0)}/100

## Next Actions
{chr(10).join(f'- {action}' for action in report.get('next_actions', []))}
"""
    st.download_button("📥 Download Markdown", data=md_content, file_name="startup_validation_report.md", mime="text/markdown", use_container_width=True)
with col3:
    if st.button("🔄 Start New Validation", use_container_width=True):
        st.session_state["backend_response"] = None
        st.session_state["report"] = None
        st.session_state["pipeline_status"] = "idle"
        st.switch_page("pages/01_Home.py")

render_page_footer()