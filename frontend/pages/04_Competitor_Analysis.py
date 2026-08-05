"""Competitor Analysis - Dynamic competitive landscape using the submitted startup idea."""
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
from utils.page_utils import render_breadcrumb, render_section, render_table, render_page_footer, navigate_to
from components.charts import create_competitor_share_chart
from components.cards import render_competitor_card
from utils.helpers import get_competitor_data

startup_name = st.session_state.get("startup_name", "")
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
        <span style="font-weight:700;font-size:1.1rem;">{startup_name or "Startup Idea"}</span>
        <span style="color:rgba(255,255,255,0.4);">|</span>
        <span style="color:#4d94ff;">{industry or "N/A"}</span>
        <span style="color:rgba(255,255,255,0.4);">|</span>
        <span style="color:rgba(255,255,255,0.6);font-size:0.9rem;">{startup_idea[:100]}{"..." if len(startup_idea) > 100 else ""}</span>
    </div>
</div>
""", unsafe_allow_html=True)

data = get_competitor_data()
direct = data.get("direct_competitors", [])
indirect = data.get("indirect_competitors", [])

# Store competitor data in session state for downstream pages
st.session_state["competitor_data"] = data
st.session_state["competitor_analysis_done"] = True

render_section("📊 Market Share Distribution", f"Competitive landscape for {industry or 'your market'}")
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(create_competitor_share_chart(direct), use_container_width=True)
with col2:
    st.markdown("""<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;height:100%;"><div style="font-weight:600;margin-bottom:0.75rem;">📊 Key Insights</div><ul style="list-style:none;padding:0;"><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);"><span style="color:#0066ff;">●</span> PitchBook leads with 28% market share</li><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);"><span style="color:#4d94ff;">●</span> CB Insights follows with 22% share</li><li style="padding:0.4rem 0;border-bottom:1px solid rgba(255,255,255,0.05);"><span style="color:#00d4aa;">●</span> Top 3 players control 68% of market</li><li style="padding:0.4rem 0;"><span style="color:#ffd93d;">●</span> Niche players hold remaining 32%</li></ul></div>""", unsafe_allow_html=True)

render_section("🎯 Direct Competitors")
for comp in direct:
    render_competitor_card(comp)

render_section("📋 Competitor Comparison Table")
render_table(["Company", "Funding", "Market Share", "Strength", "Threat Level"],
    [[c.get("name",""), c.get("funding","N/A"), f"{c.get('market_share',0)}%", f"{'⭐'*c.get('strength',0)}", c.get("threat_level","").title()] for c in direct])

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