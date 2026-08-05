"""
Web Search Agent - AI-powered search using DuckDuckGo.
Uses the startup idea from the Home page form. No static descriptions.
"""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Web Search Agent", page_icon="🌐", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()

from utils.page_utils import render_breadcrumb, render_section, render_page_footer, navigate_to
import time
from utils.helpers import get_search_results

render_breadcrumb("🌐 Web Search Agent")

# Check if startup idea exists in session state
startup_name = st.session_state.get("startup_name", "")
startup_idea = st.session_state.get("startup_idea", "")
industry = st.session_state.get("industry", "")
country = st.session_state.get("country", "")

if not startup_idea:
    st.warning("⚠️ Please enter your startup idea first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

# Display current startup info
st.markdown(f"""
<div style="background:linear-gradient(135deg,rgba(0,102,255,0.08),rgba(0,212,170,0.08));
    border:1px solid rgba(0,102,255,0.2);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem;">
    <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1rem;">
        <span style="font-size:1.5rem;">💡</span>
        <span style="font-size:1.1rem;font-weight:700;color:#fff;">Current Startup</span>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;">
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem;">
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Startup Name</div>
            <div style="font-size:1rem;font-weight:600;color:#4d94ff;">{startup_name or "N/A"}</div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem;">
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Startup Idea</div>
            <div style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{startup_idea[:120]}{"..." if len(startup_idea) > 120 else ""}</div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem;">
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Industry</div>
            <div style="font-size:1rem;font-weight:600;color:#00d4aa;">{industry or "N/A"}</div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem;">
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Country</div>
            <div style="font-size:1rem;font-weight:600;color:#ffd93d;">{country or "N/A"}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Search Pipeline Execution
render_section("🔍 Search Pipeline", f"Running analysis for: {startup_name or startup_idea[:50]}")

search_stages = [
    ("💡", "User Idea", "Your startup concept received"),
    ("🔧", "Query Generation", "Generating optimized search queries..."),
    ("🦆", "DuckDuckGo Search", "Searching the web for market data..."),
    ("📰", "Market Articles", "Collecting latest market news and articles..."),
    ("🏢", "Competitor Discovery", "Identifying competing companies..."),
    ("💬", "Customer Discussions", "Analyzing customer conversations..."),
    ("📊", "Source Ranking", "Ranking by relevance and credibility..."),
    ("🎯", "Deduplication", "Removing duplicate information..."),
    ("📋", "Structured Results", "Preparing structured output data..."),
]

progress_bar = st.progress(0)
status_placeholder = st.empty()

for i, (icon, label, desc) in enumerate(search_stages):
    progress = (i + 1) / len(search_stages)
    progress_bar.progress(progress)
    status_placeholder.markdown(
        f'<div style="text-align:center;padding:1rem;background:rgba(0,102,255,0.05);'
        f'border:1px solid rgba(0,102,255,0.15);border-radius:12px;margin:0.5rem 0;">'
        f'<span style="font-size:1.5rem;">{icon}</span> '
        f'<span style="font-weight:600;">{label}</span> — '
        f'<span style="color:rgba(255,255,255,0.6);">{desc}</span></div>',
        unsafe_allow_html=True
    )
    time.sleep(0.4)

progress_bar.progress(1.0)
status_placeholder.success("✅ Search pipeline complete! Results ready for analysis.")
time.sleep(0.5)
status_placeholder.empty()

# Load search results
data = get_search_results()
articles = data.get("articles", [])
competitors = data.get("competitors", [])
funding_news = data.get("funding_news", [])
discussions = data.get("discussions", [])
industry_reports = data.get("industry_reports", [])
stats = data.get("market_statistics", {})

# Store in session state for downstream pages
st.session_state["search_results"] = data
st.session_state["search_completed"] = True

# Metrics
render_section("📊 Search Results Overview", f"Found {stats.get('total_articles_found', 0)} documents across {len(stats.get('sources_used', []))} sources")

metrics = [
    ("📰", "Articles Found", str(stats.get("total_articles_found", 0))),
    ("🏢", "Competitors", str(stats.get("total_competitors_identified", 0))),
    ("💰", "Funding Rounds", str(stats.get("total_funding_rounds", 0))),
    ("💬", "Discussions", str(stats.get("total_discussions_analyzed", 0))),
]
cols = st.columns(4)
for i, (icon, label, value) in enumerate(metrics):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;"><div style="font-size:1.5rem;">{icon}</div><div style="font-size:1.25rem;font-weight:700;color:#4d94ff;">{value}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{label}</div></div>', unsafe_allow_html=True)

# Market Articles
if articles:
    render_section("📰 Market Articles", "Latest news and articles about your market")
    from components.cards import render_article_card
    for article in articles[:6]:
        render_article_card(article)

# Competitors Found
if competitors:
    render_section("🏢 Competitors Discovered", "Companies operating in your space")
    from components.cards import render_competitor_card
    for comp in competitors[:5]:
        render_competitor_card(comp)

# Funding News
if funding_news:
    render_section("💰 Funding News", "Recent investment activities in your industry")
    from components.cards import render_funding_card
    for funding in funding_news:
        render_funding_card(funding)

# Discussions
if discussions:
    render_section("💬 Customer Discussions", "What customers are saying")
    from components.cards import render_discussion_card
    for discussion in discussions:
        render_discussion_card(discussion)

# Industry Reports
if industry_reports:
    render_section("📊 Industry Reports", "Market research reports")
    from components.cards import render_report_card
    for report in industry_reports:
        render_report_card(report)

# Navigation to next pages
render_section("▶️ Continue Analysis", "Proceed to the next analysis stages")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📈 Market Analysis →", use_container_width=True):
        navigate_to("03_Market_Analysis.py")
with col2:
    if st.button("🏆 Competitor Analysis →", use_container_width=True):
        navigate_to("04_Competitor_Analysis.py")
with col3:
    if st.button("📄 Final Report →", use_container_width=True):
        navigate_to("08_Report.py")

render_page_footer()