"""Market Analysis - Dynamic market intelligence using the submitted startup idea."""
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
from utils.page_utils import render_breadcrumb, render_section, render_table, render_page_footer, navigate_to
from components.charts import create_market_size_chart, create_growth_chart, create_market_segment_chart, create_revenue_projection_chart
from components.metrics import render_metric_row
from utils.helpers import get_market_data

startup_name = st.session_state.get("startup_name", "")
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
        <span style="font-weight:700;font-size:1.1rem;">{startup_name or "Startup Idea"}</span>
        <span style="color:rgba(255,255,255,0.4);">|</span>
        <span style="color:#4d94ff;">{industry or "N/A"}</span>
        <span style="color:rgba(255,255,255,0.4);">|</span>
        <span style="color:rgba(255,255,255,0.6);font-size:0.9rem;">{startup_idea[:100]}{"..." if len(startup_idea) > 100 else ""}</span>
    </div>
</div>
""", unsafe_allow_html=True)

data = get_market_data()
overview = data.get("market_overview", {})
segments = data.get("market_segments", [])
trends = data.get("industry_trends", {})
revenue = data.get("revenue_projection", {})

# Store market data in session state for downstream pages
st.session_state["market_data"] = data
st.session_state["market_analysis_done"] = True

render_section("📊 Key Market Metrics", f"Critical indicators for {industry or 'your market'}")
metrics = [
    ("TAM", overview.get("total_addressable_market","N/A"), "22.4% CAGR", "🌍"),
    ("SAM", overview.get("serviceable_addressable_market","N/A"), "Growing", "🎯"),
    ("SOM", overview.get("serviceable_obtainable_market","N/A"), "Achievable", "✅"),
    ("Growth Rate", overview.get("market_growth_rate","N/A"), "High", "📈")
]
render_metric_row(metrics)

render_section("📈 Market Size & Growth", "Visual analysis")
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(create_market_size_chart(trends.get("years",[]), trends.get("market_sizes",[]), "Market Size ($B)"), use_container_width=True)
with col2:
    st.plotly_chart(create_growth_chart(trends.get("years",[]), trends.get("ai_adoption_rate",[]), "AI Adoption Rate (%)"), use_container_width=True)

render_section("🎯 Target Audience & Segments", "Market breakdown")
col1, col2 = st.columns([3,2])
with col1:
    st.plotly_chart(create_market_segment_chart(segments), use_container_width=True)
with col2:
    for s in segments:
        st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:0.75rem;margin-bottom:0.5rem;"><div style="display:flex;justify-content:space-between;"><div><div style="font-weight:600;font-size:0.9rem;">{s.get("name","")}</div><div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{", ".join(s.get("customers",[])[:2])}</div></div><div style="text-align:right;"><div style="font-size:1rem;font-weight:700;color:#4d94ff;">{s.get("size","")}</div><div style="font-size:0.75rem;color:#00d4aa;">📈 {s.get("growth","")}</div></div></div></div>', unsafe_allow_html=True)

render_section("💰 Revenue Forecast", "5-year projection")
st.plotly_chart(create_revenue_projection_chart(revenue), use_container_width=True)

render_section("📋 Market Concepts Explained", "Key terminology")
render_table(["Term", "Definition", "Current Value"], [
    ["TAM", "Total Addressable Market - total revenue opportunity", overview.get("total_addressable_market","N/A")],
    ["SAM", "Serviceable Addressable Market - segment you can reach", overview.get("serviceable_addressable_market","N/A")],
    ["SOM", "Serviceable Obtainable Market - what you can capture", overview.get("serviceable_obtainable_market","N/A")],
    ["CAGR", "Compound Annual Growth Rate over 5 years", overview.get("cagr_5year","N/A")],
    ["Market Maturity", "Current stage of market development", overview.get("market_maturity","N/A")],
    ["Growth Rate", "Annual market growth percentage", overview.get("market_growth_rate","N/A")],
])

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