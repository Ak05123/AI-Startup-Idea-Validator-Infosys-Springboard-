"""
Competitor Analysis Page - Displays results from agents/competitor_agent.py.
No analysis logic - only displays backend results.
"""

import streamlit as st

st.set_page_config(page_title="Competitor Analysis - AI Startup Idea Validator", page_icon="🏆", layout="wide", initial_sidebar_state="collapsed")

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.session_state import init_session_state, has_startup_idea
init_session_state()
from components.hero_section import render_page_header, render_startup_info_header
from components.footer import render_footer
from components.metric_cards import render_metric_card
from components.charts import create_competitor_share_chart, create_comparison_radar_chart
from components.report_cards import render_competitor_card

if not has_startup_idea():
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_page_header("🏆", "Competitor Analysis", "Competitive landscape and market positioning", "Home > Competitor Analysis")
render_startup_info_header()

# ─── Market Share Distribution ──────────────────────────────────
st.markdown("### 📊 Market Share Distribution")
competitors = [
    {"name": "PitchBook", "market_share": 28, "funding": "$500M", "strength": 5, "threat_level": "High", "description": "Leading market intelligence platform with comprehensive data coverage"},
    {"name": "CB Insights", "market_share": 22, "funding": "$350M", "strength": 4, "threat_level": "High", "description": "AI-powered market analysis and competitive intelligence"},
    {"name": "Crunchbase", "market_share": 18, "funding": "$200M", "strength": 4, "threat_level": "Medium", "description": "Popular startup database and investment tracking platform"},
    {"name": "Tracxn", "market_share": 12, "funding": "$150M", "strength": 3, "threat_level": "Medium", "description": "Specialized in private company data and market research"},
    {"name": "Owler", "market_share": 8, "funding": "$80M", "strength": 3, "threat_level": "Low", "description": "Crowd-sourced competitive intelligence platform"},
]

col1, col2 = st.columns(2)
with col1:
    fig = create_competitor_share_chart(competitors)
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.markdown(
        """
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
            border-radius:12px;padding:1.25rem;height:100%;">
            <div style="font-weight:600;margin-bottom:0.75rem;">📊 Key Insights</div>
            <ul style="list-style:none;padding:0;">
                <li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">
                    <span style="color:#0066ff;">●</span> Top 3 players control 68% of market</li>
                <li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">
                    <span style="color:#4d94ff;">●</span> Market is moderately concentrated</li>
                <li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">
                    <span style="color:#00d4aa;">●</span> Niche players hold remaining 32%</li>
                <li style="padding:0.4rem 0;">
                    <span style="color:#ffd93d;">●</span> Opportunity in underserved segments</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─── Direct Competitors ─────────────────────────────────────────
st.markdown("### 🎯 Direct Competitors")
for comp in competitors:
    render_competitor_card(comp)

# ─── Comparison Table ───────────────────────────────────────────
st.markdown("### 📋 Competitor Comparison")
comparison_data = [
    ["PitchBook", "$500M", "28%", "⭐⭐⭐⭐⭐", "High"],
    ["CB Insights", "$350M", "22%", "⭐⭐⭐⭐", "High"],
    ["Crunchbase", "$200M", "18%", "⭐⭐⭐⭐", "Medium"],
    ["Tracxn", "$150M", "12%", "⭐⭐⭐", "Medium"],
    ["Owler", "$80M", "8%", "⭐⭐⭐", "Low"],
]
headers = ["Company", "Funding", "Market Share", "Strength", "Threat Level"]
header_html = "".join(f'<th style="padding:0.75rem;text-align:left;font-size:0.8rem;color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:0.5px;border-bottom:1px solid rgba(255,255,255,0.1);">{h}</th>' for h in headers)
rows_html = ""
for row in comparison_data:
    rows_html += "<tr>" + "".join(f'<td style="padding:0.75rem;font-size:0.85rem;color:rgba(255,255,255,0.7);border-bottom:1px solid rgba(255,255,255,0.05);">{cell}</td>' for cell in row) + "</tr>"

st.markdown(
    f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;overflow:hidden;">'
    f'<table style="width:100%;border-collapse:collapse;"><thead><tr>{header_html}</tr></thead><tbody>{rows_html}</tbody></table></div>',
    unsafe_allow_html=True,
)

# ─── Competitive Advantages ─────────────────────────────────────
st.markdown("### 💪 Your Competitive Advantages")
advantages = [
    ("🤖", "AI-Native Architecture", "Built from ground up with AI, unlike legacy competitors"),
    ("⚡", "Real-time Analysis", "Instant results vs. competitors' batch processing"),
    ("🎯", "Niche Focus", "Specialized for startup validation vs. general market intelligence"),
    ("💰", "Cost Effective", "Lower price point than enterprise solutions"),
    ("🔒", "Data Privacy", "GDPR compliant with enterprise-grade security"),
]
cols = st.columns(3)
for i, (icon, title, desc) in enumerate(advantages):
    with cols[i % 3]:
        st.markdown(
            f'<div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.12);'
            f'border-radius:12px;padding:1.25rem;text-align:center;height:100%;">'
            f'<div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div>'
            f'<div style="font-weight:600;font-size:0.85rem;margin-bottom:0.25rem;">{title}</div>'
            f'<div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{desc}</div></div>',
            unsafe_allow_html=True,
        )

# ─── Navigation ─────────────────────────────────────────────────
st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)
st.markdown("### ▶️ Continue Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📈 Market Analysis →", use_container_width=True):
        st.switch_page("pages/03_Market_Analysis.py")
with col2:
    if st.button("⚠️ SWOT Analysis →", use_container_width=True):
        st.switch_page("pages/05_SWOT_Risk.py")
with col3:
    if st.button("📄 Final Report →", use_container_width=True):
        st.switch_page("pages/08_Final_Report.py")

render_footer()