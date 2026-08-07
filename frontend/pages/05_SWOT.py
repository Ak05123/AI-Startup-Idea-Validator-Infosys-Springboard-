"""SWOT Analysis - Displays results from the backend swot_risk_agent.py."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="SWOT Analysis", page_icon="⚠️", layout="wide", initial_sidebar_state="expanded")
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

if not startup_idea:
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_breadcrumb("⚠️ SWOT Analysis")

# Startup info header
st.markdown(f"""
<div style="background:linear-gradient(135deg,rgba(0,102,255,0.08),rgba(0,212,170,0.08));
    border:1px solid rgba(0,102,255,0.2);border-radius:16px;padding:1.25rem;margin-bottom:1rem;">
    <div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap;">
        <span style="font-size:1.5rem;">💡</span>
        <span style="font-weight:700;font-size:1.1rem;">Startup Idea</span>
        <span style="color:rgba(255,255,255,0.4);">|</span>
        <span style="color:#4d94ff;">{industry or "N/A"}</span>
        <span style="color:rgba(255,255,255,0.4);">|</span>
        <span style="color:rgba(255,255,255,0.6);font-size:0.9rem;">{startup_idea[:100]}{"..." if len(startup_idea) > 100 else ""}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Get backend response
backend_response = st.session_state.get("backend_response")
if not backend_response:
    st.warning("⚠️ No analysis results found. Please run the validation from the Web Search page first.")
    if st.button("🌐 Go to Web Search", use_container_width=True):
        navigate_to("02_Web_Search_Agent.py")
    st.stop()

# Parse SWOT from backend
swot_raw = backend_response.get("swot_analysis", "{}")
swot = parse_json_response(swot_raw)

if swot.get("raw") is not None:
    st.info("SWOT analysis data is not available in structured format.")
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">{swot.get("raw", "")}</div>', unsafe_allow_html=True)
else:
    def render_swot_quadrant(title, items, icon, color):
        items_html = "".join(f'<div style="padding:0.5rem 0;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;align-items:flex-start;gap:0.5rem;"><span style="color:{color};font-size:1rem;">▸</span><span style="font-size:0.85rem;color:rgba(255,255,255,0.7);">{item}</span></div>' for item in items)
        st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid {color}33;border-radius:12px;padding:1.25rem;height:100%;"><div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.75rem;"><span style="font-size:1.5rem;">{icon}</span><span style="font-size:1rem;font-weight:700;color:{color};">{title}</span></div>{items_html}</div>', unsafe_allow_html=True)

    render_section("📊 SWOT Analysis", "Strategic analysis from the SWOT & Risk Agent")

    col1, col2 = st.columns(2)
    with col1:
        render_swot_quadrant("Strengths", swot.get("strengths", []), "💪", "#00d4aa")
    with col2:
        render_swot_quadrant("Weaknesses", swot.get("weaknesses", []), "⚠️", "#ff6b6b")

    col1, col2 = st.columns(2)
    with col1:
        render_swot_quadrant("Opportunities", swot.get("opportunities", []), "🚀", "#4d94ff")
    with col2:
        render_swot_quadrant("Threats", swot.get("threats", []), "🔥", "#ffd93d")

    # Business Risks
    risks = swot.get("risks", [])
    if risks:
        render_section("⚠️ Business Risks", "Key risks identified by the backend")
        for risk in risks:
            st.markdown(f'<div style="background:rgba(255,107,107,0.05);border:1px solid rgba(255,107,107,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">⚠️</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{risk}</span></div>', unsafe_allow_html=True)

# Navigation
render_section("▶️ Continue Analysis", "Proceed to the next analysis stages")
col1, col2 = st.columns(2)
with col1:
    if st.button("💡 MVP Recommendation →", use_container_width=True):
        navigate_to("06_MVP.py")
with col2:
    if st.button("📄 Final Report →", use_container_width=True):
        navigate_to("08_Report.py")

render_page_footer()