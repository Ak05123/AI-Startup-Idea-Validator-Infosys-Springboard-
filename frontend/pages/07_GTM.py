"""GTM Strategy - Displays results from the backend gtm_strategy_agent.py."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="GTM Strategy", page_icon="📢", layout="wide", initial_sidebar_state="expanded")
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

render_breadcrumb("📢 GTM Strategy")

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

# Parse GTM from backend
gtm_raw = backend_response.get("gtm_strategy", "{}")
gtm = parse_json_response(gtm_raw)

if gtm.get("raw") is not None:
    st.info("GTM strategy data is not available in structured format.")
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">{gtm.get("raw", "")}</div>', unsafe_allow_html=True)
else:
    # Target Market
    target_market = gtm.get("target_market", [])
    if target_market:
        render_section("🎯 Target Market", "Markets to focus on")
        for market in target_market:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">🎯</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{market}</span></div>', unsafe_allow_html=True)

    # Primary Customer Segment
    primary_segment = gtm.get("primary_customer_segment", "")
    if primary_segment:
        render_section("👥 Primary Customer Segment", "Initial target customer")
        st.markdown(f'<div style="background:rgba(0,102,255,0.05);border:1px solid rgba(0,102,255,0.15);border-radius:12px;padding:1.25rem;font-size:0.95rem;color:rgba(255,255,255,0.8);line-height:1.7;">{primary_segment}</div>', unsafe_allow_html=True)

    # Value Proposition
    value_prop = gtm.get("value_proposition", "")
    if value_prop:
        render_section("💎 Value Proposition", "Core value delivered to customers")
        st.markdown(f'<div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);border-radius:12px;padding:1.25rem;font-size:0.95rem;color:rgba(255,255,255,0.8);line-height:1.7;">{value_prop}</div>', unsafe_allow_html=True)

    # Positioning
    positioning = gtm.get("positioning", "")
    if positioning:
        render_section("📍 Positioning", "How the startup should be positioned")
        st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;font-size:0.95rem;color:rgba(255,255,255,0.8);line-height:1.7;">{positioning}</div>', unsafe_allow_html=True)

    # Pricing Strategy
    pricing = gtm.get("pricing_strategy", "")
    if pricing:
        render_section("💰 Pricing Strategy", "Recommended pricing approach")
        st.markdown(f'<div style="background:rgba(255,217,61,0.05);border:1px solid rgba(255,217,61,0.15);border-radius:12px;padding:1.25rem;font-size:0.95rem;color:rgba(255,255,255,0.8);line-height:1.7;">{pricing}</div>', unsafe_allow_html=True)

    # Customer Acquisition Channels
    channels = gtm.get("customer_acquisition_channels", [])
    if channels:
        render_section("📡 Customer Acquisition Channels", "Channels to reach customers")
        for channel in channels:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">📡</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{channel}</span></div>', unsafe_allow_html=True)

    # Launch Strategy
    launch_strategy = gtm.get("launch_strategy", [])
    if launch_strategy:
        render_section("🚀 Launch Strategy", "Phased launch plan")
        for i, step in enumerate(launch_strategy):
            st.markdown(f'<div style="background:rgba(77,148,255,0.05);border:1px solid rgba(77,148,255,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;color:#4d94ff;font-weight:700;">{i + 1}</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{step}</span></div>', unsafe_allow_html=True)

    # Partnership Strategy
    partnerships = gtm.get("partnership_strategy", [])
    if partnerships:
        render_section("🤝 Partnership Strategy", "Partnership opportunities")
        for partner in partnerships:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">🤝</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{partner}</span></div>', unsafe_allow_html=True)

    # Retention Strategy
    retention = gtm.get("retention_strategy", [])
    if retention:
        render_section("🔄 Retention Strategy", "Customer retention approaches")
        for item in retention:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">🔄</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{item}</span></div>', unsafe_allow_html=True)

    # Key Metrics
    key_metrics = gtm.get("key_metrics", [])
    if key_metrics:
        render_section("📊 Key Metrics", "Metrics to track GTM success")
        for metric in key_metrics:
            st.markdown(f'<div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">📊</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{metric}</span></div>', unsafe_allow_html=True)

    # Major GTM Risks
    gtm_risks = gtm.get("major_gtm_risks", [])
    if gtm_risks:
        render_section("⚠️ Major GTM Risks", "Risks to monitor")
        for risk in gtm_risks:
            st.markdown(f'<div style="background:rgba(255,107,107,0.05);border:1px solid rgba(255,107,107,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">⚠️</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{risk}</span></div>', unsafe_allow_html=True)

# Navigation
render_section("▶️ Continue Analysis", "Proceed to the next analysis stages")
col1, col2 = st.columns(2)
with col1:
    if st.button("📄 Final Report →", use_container_width=True):
        navigate_to("08_Report.py")
with col2:
    if st.button("🤖 AI Advisor →", use_container_width=True):
        navigate_to("09_AI_Advisor.py")

render_page_footer()