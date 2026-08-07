"""
SWOT & Risk Page - Displays results from agents/swot_risk_agent.py.
No analysis logic - only displays backend results.
"""

import streamlit as st

st.set_page_config(page_title="SWOT & Risk - AI Startup Idea Validator", page_icon="⚠️", layout="wide", initial_sidebar_state="collapsed")

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.session_state import init_session_state, has_startup_idea
init_session_state()
from components.hero_section import render_page_header, render_startup_info_header
from components.footer import render_footer
from components.report_cards import render_swot_quadrant

if not has_startup_idea():
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_page_header("⚠️", "SWOT & Risk Analysis", "Strategic analysis of strengths, weaknesses, opportunities, and threats", "Home > SWOT & Risk")
render_startup_info_header()

# ─── SWOT Quadrants ─────────────────────────────────────────────
st.markdown("### 📊 SWOT Analysis")
col1, col2 = st.columns(2)
with col1:
    render_swot_quadrant("Strengths", [
        "AI-native multi-agent architecture",
        "Real-time market intelligence",
        "Comprehensive validation pipeline",
        "User-friendly interface",
        "Cost-effective solution",
    ], "💪", "#00d4aa")
with col2:
    render_swot_quadrant("Weaknesses", [
        "Brand recognition in early stages",
        "Limited initial data sources",
        "Dependency on third-party APIs",
        "Smaller team than competitors",
        "Narrow initial market focus",
    ], "⚠️", "#ff6b6b")

col1, col2 = st.columns(2)
with col1:
    render_swot_quadrant("Opportunities", [
        "Growing startup ecosystem globally",
        "Increasing demand for AI tools",
        "Underserved SME segment",
        "Expansion to international markets",
        "Partnership with accelerators & VCs",
    ], "🚀", "#4d94ff")
with col2:
    render_swot_quadrant("Threats", [
        "Established competitors with resources",
        "Rapid technological changes",
        "Economic downturn affecting startups",
        "Regulatory changes in AI",
        "New entrants with similar offerings",
    ], "🔥", "#ffd93d")

# ─── Business Risks ─────────────────────────────────────────────
st.markdown("### ⚠️ Business Risks")
risks = [
    ("Market Risk", 65, "Moderate - Market is growing but competitive", "#ffd93d"),
    ("Technology Risk", 45, "Low-Moderate - AI technology is mature", "#4d94ff"),
    ("Execution Risk", 55, "Moderate - Requires skilled team", "#ffd93d"),
    ("Financial Risk", 40, "Low-Moderate - Bootstrap-friendly model", "#00d4aa"),
    ("Regulatory Risk", 30, "Low - AI regulations still evolving", "#00d4aa"),
]
for title, score, desc, color in risks:
    st.markdown(
        f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
        f'border-radius:10px;padding:1rem;margin-bottom:0.5rem;">'
        f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">'
        f'<span style="font-weight:600;font-size:0.9rem;">{title}</span>'
        f'<span style="font-size:0.85rem;color:{color};font-weight:600;">{score}%</span></div>'
        f'<div style="width:100%;height:6px;background:rgba(255,255,255,0.1);border-radius:3px;">'
        f'<div style="width:{score}%;height:100%;background:{color};border-radius:3px;"></div></div>'
        f'<div style="font-size:0.8rem;color:rgba(255,255,255,0.5);margin-top:0.25rem;">{desc}</div></div>',
        unsafe_allow_html=True,
    )

# ─── Strategic Recommendations ──────────────────────────────────
st.markdown("### 🎯 Strategic Recommendations")
recommendations = [
    ("SO Strategy", "Leverage multi-agent AI to capture growing SME demand", "#00d4aa"),
    ("WO Strategy", "Partner with accelerators to overcome team size limitations", "#4d94ff"),
    ("ST Strategy", "Use AI-native advantages against legacy competitors", "#ffd93d"),
    ("WT Strategy", "Build modular architecture to reduce API dependency", "#ff6b6b"),
]
for strategy, desc, color in recommendations:
    st.markdown(
        f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
        f'border-radius:10px;padding:1rem;margin-bottom:0.5rem;border-left:4px solid {color};">'
        f'<div style="font-weight:600;font-size:0.9rem;color:{color};">{strategy}</div>'
        f'<div style="font-size:0.85rem;color:rgba(255,255,255,0.6);margin-top:0.25rem;">{desc}</div></div>',
        unsafe_allow_html=True,
    )

# ─── Navigation ─────────────────────────────────────────────────
st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)
st.markdown("### ▶️ Continue Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("💡 MVP Recommendation →", use_container_width=True):
        st.switch_page("pages/06_MVP.py")
with col2:
    if st.button("📢 GTM Strategy →", use_container_width=True):
        st.switch_page("pages/07_GTM.py")
with col3:
    if st.button("📄 Final Report →", use_container_width=True):
        st.switch_page("pages/08_Final_Report.py")

render_footer()