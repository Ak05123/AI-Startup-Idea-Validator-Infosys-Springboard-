"""Competitor Analysis - Displays results from the backend competitor_agent.py."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Competitor Analysis", page_icon="🏆", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()
from utils.page_utils import render_breadcrumb, render_section, render_page_footer, navigate_to
from utils.backend_client import parse_list_response

startup_idea = st.session_state.get("startup_idea", "")
industry = st.session_state.get("industry", "")

if not startup_idea:
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_breadcrumb("🏆 Competitor Analysis")

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

# Parse competitors from backend
competitors_raw = backend_response.get("competitors", [])
competitors = parse_list_response(competitors_raw)

if not competitors:
    st.info("No competitors identified by the backend.")
else:
    # Competitors List
    render_section("🎯 Competitors Identified", f"Companies identified by the Competitor Agent")
    for comp in competitors:
        st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.5rem;">🏢</span><div><div style="font-weight:600;font-size:0.95rem;">{comp}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Direct competitor</div></div></div>', unsafe_allow_html=True)

    # Comparison Table
    render_section("📋 Competitor Comparison", "Identified competitors overview")
    headers = ["#", "Competitor", "Status"]
    rows = [[str(i + 1), comp, "Identified"] for i, comp in enumerate(competitors)]
    header_html = "".join(f'<th style="padding:0.6rem 0.75rem;text-align:left;font-size:0.8rem;color:rgba(255,255,255,0.5);border-bottom:1px solid rgba(255,255,255,0.1);font-weight:500;">{h}</th>' for h in headers)
    rows_html = ""
    for row in rows:
        rows_html += "<tr>" + "".join(f'<td style="padding:0.6rem 0.75rem;font-size:0.85rem;color:rgba(255,255,255,0.7);border-bottom:1px solid rgba(255,255,255,0.05);">{c}</td>' for c in row) + "</tr>"
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:0.75rem;margin:0.75rem 0;overflow-x:auto;"><table style="width:100%;border-collapse:collapse;">{header_html}{rows_html}</table></div>', unsafe_allow_html=True)

# Navigation
render_section("▶️ Continue Analysis", "Proceed to the next analysis stages")
col1, col2 = st.columns(2)
with col1:
    if st.button("📈 Market Analysis →", use_container_width=True):
        navigate_to("03_Market_Analysis.py")
with col2:
    if st.button("📄 Final Report →", use_container_width=True):
        navigate_to("08_Report.py")

render_page_footer()