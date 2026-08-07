"""Market Analysis - Displays results from the backend market_analysis_agent.py."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Market Analysis", page_icon="📈", layout="wide", initial_sidebar_state="expanded")
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

render_breadcrumb("📈 Market Analysis")

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

# Parse market analysis from backend
market_raw = backend_response.get("market_analysis", "{}")
market = parse_json_response(market_raw)

if market.get("raw") is not None:
    st.info("Market analysis data is not available in structured format.")
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">{market.get("raw", "")}</div>', unsafe_allow_html=True)
else:
    # Key Market Metrics
    render_section("📊 Key Market Metrics", f"Critical indicators for {industry or 'your market'}")
    col1, col2, col3, col4 = st.columns(4)
    metrics = [
        ("🌍", "Industry", market.get("industry", "N/A")),
        ("📈", "Market Size", market.get("market_size", "N/A")),
        ("🚀", "Growth Rate", market.get("growth_rate", "N/A")),
        ("🎯", "Target Customers", str(len(market.get("target_customers", []))) + " segments"),
    ]
    for i, (icon, label, value) in enumerate(metrics):
        with [col1, col2, col3, col4][i]:
            st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;"><div style="font-size:1.5rem;">{icon}</div><div style="font-size:1.25rem;font-weight:700;color:#4d94ff;">{value}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{label}</div></div>', unsafe_allow_html=True)

    # Target Customers
    target_customers = market.get("target_customers", [])
    if target_customers:
        render_section("🎯 Target Customers", "Identified customer segments")
        cols = st.columns(2)
        for i, customer in enumerate(target_customers):
            with cols[i % 2]:
                st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;"><div style="font-size:0.9rem;font-weight:600;">👥 {customer}</div></div>', unsafe_allow_html=True)

    # Market Trends
    market_trends = market.get("market_trends", [])
    if market_trends:
        render_section("📈 Market Trends", "Current industry trends")
        for trend in market_trends:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">📈</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{trend}</span></div>', unsafe_allow_html=True)

    # Opportunities
    opportunities = market.get("opportunities", [])
    if opportunities:
        render_section("🚀 Opportunities", "Business opportunities identified")
        for opp in opportunities:
            st.markdown(f'<div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">🚀</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{opp}</span></div>', unsafe_allow_html=True)

    # Challenges
    challenges = market.get("challenges", [])
    if challenges:
        render_section("⚠️ Challenges", "Market challenges to address")
        for challenge in challenges:
            st.markdown(f'<div style="background:rgba(255,107,107,0.05);border:1px solid rgba(255,107,107,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">⚠️</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{challenge}</span></div>', unsafe_allow_html=True)

# Navigation
render_section("▶️ Continue Analysis", "Proceed to the next analysis stages")
col1, col2 = st.columns(2)
with col1:
    if st.button("🏆 Competitor Analysis →", use_container_width=True):
        navigate_to("04_Competitor_Analysis.py")
with col2:
    if st.button("📄 Final Report →", use_container_width=True):
        navigate_to("08_Report.py")

render_page_footer()