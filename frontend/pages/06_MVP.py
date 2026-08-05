"""MVP Recommendation - Displays results from the backend mvp_recommendation_agent.py."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="MVP Recommendation", page_icon="💡", layout="wide", initial_sidebar_state="expanded")
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

render_breadcrumb("💡 MVP Recommendation")

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

# Parse MVP from backend
mvp_raw = backend_response.get("mvp_recommendation", "{}")
mvp = parse_json_response(mvp_raw)

if mvp.get("raw") is not None:
    st.info("MVP recommendation data is not available in structured format.")
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">{mvp.get("raw", "")}</div>', unsafe_allow_html=True)
else:
    # MVP Goal
    mvp_goal = mvp.get("mvp_goal", "")
    if mvp_goal:
        render_section("🎯 MVP Goal", "Primary objective of the MVP")
        st.markdown(f'<div style="background:rgba(0,102,255,0.05);border:1px solid rgba(0,102,255,0.15);border-radius:12px;padding:1.25rem;font-size:0.95rem;color:rgba(255,255,255,0.8);line-height:1.7;">{mvp_goal}</div>', unsafe_allow_html=True)

    # Primary MVP Users
    primary_users = mvp.get("primary_mvp_users", [])
    if primary_users:
        render_section("👥 Primary MVP Users", "Initial customer segment")
        for user in primary_users:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">👥</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{user}</span></div>', unsafe_allow_html=True)

    # Core Features
    core_features = mvp.get("core_features", [])
    if core_features:
        render_section("🎯 Core Features", "Priority features for the MVP")
        for feat in core_features:
            st.markdown(f'<div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">✅</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{feat}</span></div>', unsafe_allow_html=True)

    # Secondary Features
    secondary_features = mvp.get("secondary_features", [])
    if secondary_features:
        render_section("🔧 Secondary Features", "Additional features for later phases")
        for feat in secondary_features:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">🔧</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{feat}</span></div>', unsafe_allow_html=True)

    # Features to Avoid
    features_to_avoid = mvp.get("features_to_avoid_initially", [])
    if features_to_avoid:
        render_section("🚫 Features to Avoid Initially", "Features to defer")
        for feat in features_to_avoid:
            st.markdown(f'<div style="background:rgba(255,107,107,0.05);border:1px solid rgba(255,107,107,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">🚫</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{feat}</span></div>', unsafe_allow_html=True)

    # Development Priority
    dev_priority = mvp.get("development_priority", [])
    if dev_priority:
        render_section("📅 Development Priority", "Recommended development order")
        for i, item in enumerate(dev_priority):
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;color:#4d94ff;font-weight:700;">{i + 1}</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{item}</span></div>', unsafe_allow_html=True)

    # Validation Metrics
    validation_metrics = mvp.get("validation_metrics", [])
    if validation_metrics:
        render_section("📊 Validation Metrics", "Metrics to measure MVP success")
        for metric in validation_metrics:
            st.markdown(f'<div style="background:rgba(77,148,255,0.05);border:1px solid rgba(77,148,255,0.15);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.25rem;">📊</span><span style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{metric}</span></div>', unsafe_allow_html=True)

# Navigation
render_section("▶️ Continue Analysis", "Proceed to the next analysis stages")
col1, col2 = st.columns(2)
with col1:
    if st.button("📢 GTM Strategy →", use_container_width=True):
        navigate_to("07_GTM.py")
with col2:
    if st.button("📄 Final Report →", use_container_width=True):
        navigate_to("08_Report.py")

render_page_footer()