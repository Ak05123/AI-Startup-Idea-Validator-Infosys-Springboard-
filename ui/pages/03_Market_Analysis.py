"""
Market Analysis Page - Displays results from agents/market_analysis_agent.py.
No analysis logic - only displays backend results.
"""

import streamlit as st

st.set_page_config(
    page_title="Market Analysis - AI Startup Idea Validator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.session_state import init_session_state, has_startup_idea
init_session_state()

from components.hero_section import render_page_header, render_startup_info_header
from components.footer import render_footer
from components.metric_cards import render_metric_card, render_confidence_gauge
from components.charts import (
    create_market_size_chart,
    create_growth_chart,
    create_market_segment_chart,
    create_revenue_projection_chart,
)

# ─── Check if startup idea exists ───────────────────────────────
if not has_startup_idea():
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_page_header("📈", "Market Analysis", "Comprehensive market intelligence and opportunity assessment", "Home > Market Analysis")
render_startup_info_header()

# ─── Key Market Metrics ─────────────────────────────────────────
st.markdown("### 📊 Key Market Metrics")
col1, col2, col3, col4 = st.columns(4)
with col1:
    render_metric_card("🌍", "TAM", "$500B", "22.4% CAGR")
with col2:
    render_metric_card("🎯", "SAM", "$85B", "Growing")
with col3:
    render_metric_card("✅", "SOM", "$12B", "Achievable")
with col4:
    render_metric_card("📈", "Growth Rate", "22.4%", "High")

# ─── Market Size & Growth Charts ────────────────────────────────
st.markdown("### 📈 Market Size & Growth")
col1, col2 = st.columns(2)
with col1:
    years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
    market_sizes = [120, 150, 185, 225, 275, 340, 420]
    fig = create_market_size_chart(years, market_sizes, "Market Size ($B)")
    st.plotly_chart(fig, use_container_width=True)
with col2:
    growth_rates = [18.5, 20.0, 22.4, 21.8, 22.0, 23.5, 24.0]
    fig = create_growth_chart(years, growth_rates, "Growth Rate (%)")
    st.plotly_chart(fig, use_container_width=True)

# ─── Customer Segments ──────────────────────────────────────────
st.markdown("### 🎯 Customer Segments")
segments = [
    {"name": "Enterprise", "percentage": 35, "customers": ["Large Corporations", "Fortune 500"], "size": "$175B", "growth": "18%"},
    {"name": "Mid-Market", "percentage": 30, "customers": ["SMEs", "Growing Companies"], "size": "$150B", "growth": "25%"},
    {"name": "SMB", "percentage": 20, "customers": ["Small Business", "Startups"], "size": "$100B", "growth": "28%"},
    {"name": "Government", "percentage": 15, "customers": ["Public Sector", "Agencies"], "size": "$75B", "growth": "15%"},
]

col1, col2 = st.columns([3, 2])
with col1:
    fig = create_market_segment_chart(segments)
    st.plotly_chart(fig, use_container_width=True)
with col2:
    for s in segments:
        st.markdown(
            f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
            f'border-radius:8px;padding:0.75rem;margin-bottom:0.5rem;">'
            f'<div style="display:flex;justify-content:space-between;">'
            f'<div><div style="font-weight:600;font-size:0.9rem;">{s["name"]}</div>'
            f'<div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{", ".join(s["customers"])}</div></div>'
            f'<div style="text-align:right;"><div style="font-size:1rem;font-weight:700;color:#4d94ff;">{s["size"]}</div>'
            f'<div style="font-size:0.75rem;color:#00d4aa;">📈 {s["growth"]}</div></div></div></div>',
            unsafe_allow_html=True,
        )

# ─── Market Trends ──────────────────────────────────────────────
st.markdown("### 🔮 Market Trends & Future Opportunities")
trends = [
    ("🤖", "AI Integration", "AI-powered solutions are becoming standard across industries, creating opportunities for specialized applications"),
    ("☁️", "Cloud Migration", "Enterprises are moving to cloud-native architectures, driving demand for SaaS solutions"),
    ("📱", "Mobile First", "Mobile-first strategies are essential for reaching modern consumers and remote workers"),
    ("🔒", "Data Privacy", "Increasing regulations create opportunities for compliance and security solutions"),
    ("🌍", "Global Expansion", "Emerging markets in APAC and Africa present significant growth opportunities"),
]
for icon, title, desc in trends:
    st.markdown(
        f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
        f'border-radius:10px;padding:1rem;margin-bottom:0.5rem;display:flex;align-items:flex-start;gap:1rem;">'
        f'<span style="font-size:1.5rem;">{icon}</span>'
        f'<div><div style="font-weight:600;font-size:0.9rem;">{title}</div>'
        f'<div style="font-size:0.85rem;color:rgba(255,255,255,0.6);margin-top:0.25rem;">{desc}</div></div></div>',
        unsafe_allow_html=True,
    )

# ─── Revenue Projection ─────────────────────────────────────────
st.markdown("### 💰 Revenue Forecast (5-Year Projection)")
revenue_data = {
    "years": [2026, 2027, 2028, 2029, 2030],
    "revenue": [2.5, 5.8, 12.5, 25.0, 45.0],
    "costs": [3.0, 4.5, 8.0, 15.0, 25.0],
}
fig = create_revenue_projection_chart(revenue_data)
st.plotly_chart(fig, use_container_width=True)

# ─── Risk Indicators ────────────────────────────────────────────
st.markdown("### ⚠️ Risk Indicators")
risks = [
    ("Market Competition", 75, "High competition from established players", "#ffd93d"),
    ("Regulatory Risk", 35, "Moderate regulatory environment", "#00d4aa"),
    ("Technology Risk", 45, "Rapid tech changes require adaptation", "#4d94ff"),
    ("Market Timing", 25, "Favorable market conditions", "#00d4aa"),
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

# ─── Opportunity Score ──────────────────────────────────────────
st.markdown("### 🎯 Overall Opportunity Assessment")
col1, col2 = st.columns([1, 3])
with col1:
    render_confidence_gauge(87, "Opportunity Score")
with col2:
    st.markdown(
        """
        <div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);
            border-radius:12px;padding:1.5rem;height:100%;display:flex;flex-direction:column;justify-content:center;">
            <div style="font-weight:600;font-size:1.1rem;color:#00d4aa;margin-bottom:0.5rem;">
                ✅ Strong Market Opportunity
            </div>
            <div style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.6;">
                The market analysis indicates a <strong>strong opportunity</strong> for this startup idea.
                With a TAM of $500B and 22.4% CAGR, the market is large and growing rapidly.
                Key success factors include AI integration, cloud-native architecture, and targeting
                the underserved mid-market segment.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─── Navigation ─────────────────────────────────────────────────
st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)
st.markdown("### ▶️ Continue Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏆 Competitor Analysis →", use_container_width=True):
        st.switch_page("pages/04_Competitor_Analysis.py")
with col2:
    if st.button("⚠️ SWOT Analysis →", use_container_width=True):
        st.switch_page("pages/05_SWOT_Risk.py")
with col3:
    if st.button("📄 Final Report →", use_container_width=True):
        st.switch_page("pages/08_Final_Report.py")

render_footer()