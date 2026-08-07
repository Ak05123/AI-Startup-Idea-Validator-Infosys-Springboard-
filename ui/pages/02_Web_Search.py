"""
Web Search Page - Displays results from agents/web_search_agent.py.
No searching logic - only displays backend results.
"""

import streamlit as st

st.set_page_config(
    page_title="Web Search - AI Startup Idea Validator",
    page_icon="🌐",
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
from components.loading_animation import render_agent_timeline, render_pipeline_progress
from components.report_cards import render_article_card, render_competitor_card
from components.metric_cards import render_metric_card

import time

# ─── Check if startup idea exists ───────────────────────────────
if not has_startup_idea():
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_page_header("🌐", "Web Search Agent", "Real-time market intelligence from across the web", "Home > Web Search")
render_startup_info_header()

# ─── Run Pipeline (simulated - backend will replace) ────────────
if not st.session_state.get("search_completed", False):
    st.session_state["pipeline_status"] = "running"

    progress_bar = st.progress(0)
    status_placeholder = st.empty()
    timeline_placeholder = st.empty()

    search_stages = [
        ("💡", "User Idea", "Your startup concept received"),
        ("🔧", "Query Generation", "Generating optimized search queries..."),
        ("🌐", "Web Search", "Searching the web for market data..."),
        ("📰", "Market Articles", "Collecting latest market news and articles..."),
        ("🏢", "Competitor Discovery", "Identifying competing companies..."),
        ("💬", "Customer Discussions", "Analyzing customer conversations..."),
        ("📊", "Source Ranking", "Ranking by relevance and credibility..."),
        ("🎯", "Deduplication", "Removing duplicate information..."),
        ("📋", "Structured Results", "Preparing structured output data..."),
    ]

    for i, (icon, label, desc) in enumerate(search_stages):
        progress = (i + 1) / len(search_stages)
        progress_bar.progress(progress)
        status_placeholder.markdown(
            f'<div style="text-align:center;padding:1rem;background:rgba(0,102,255,0.05);'
            f'border:1px solid rgba(0,102,255,0.15);border-radius:12px;margin:0.5rem 0;">'
            f'<span style="font-size:1.5rem;">{icon}</span> '
            f'<span style="font-weight:600;color:#4d94ff;">{label}</span> — '
            f'<span style="color:rgba(255,255,255,0.6);">{desc}</span></div>',
            unsafe_allow_html=True,
        )
        time.sleep(0.3)

    progress_bar.progress(1.0)
    status_placeholder.success("✅ Search pipeline complete! Results ready for analysis.")
    time.sleep(0.3)
    status_placeholder.empty()

    # Store mock results for demo (backend will populate real data)
    st.session_state["search_completed"] = True
    st.session_state["pipeline_status"] = "completed"
    st.rerun()

# ─── Display Search Results ─────────────────────────────────────
st.markdown(
    """
    <div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);
        border-radius:12px;padding:1rem;margin-bottom:1.5rem;">
        <div style="display:flex;align-items:center;gap:0.75rem;">
            <span style="font-size:1.25rem;">✅</span>
            <span style="font-weight:600;color:#00d4aa;">Web Search Complete</span>
            <span style="font-size:0.8rem;color:rgba(255,255,255,0.4);">
                Results from backend agents/web_search_agent.py
            </span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─── Search Results Overview Metrics ────────────────────────────
st.markdown("### 📊 Search Results Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    render_metric_card("📰", "Articles Found", "24", "From 12 sources")
with col2:
    render_metric_card("🏢", "Competitors", "8", "Direct & Indirect")
with col3:
    render_metric_card("💰", "Funding Rounds", "15", "Last 6 months")
with col4:
    render_metric_card("💬", "Discussions", "42", "From forums & social")

# ─── Search Queries ─────────────────────────────────────────────
st.markdown("### 🔍 Search Queries Executed")
queries = [
    f"'{st.session_state.get('startup_idea', 'startup')[:50]} {st.session_state.get('industry', '')} market size 2026'",
    f"'{st.session_state.get('industry', '')} industry trends and growth'",
    f"'competitors in {st.session_state.get('industry', '')} space'",
    f"'{st.session_state.get('industry', '')} funding news 2026'",
    f"'{st.session_state.get('startup_idea', 'startup')[:50]} customer reviews discussions'",
]
for q in queries:
    st.markdown(
        f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
        f'border-radius:8px;padding:0.5rem 0.75rem;margin-bottom:0.3rem;font-size:0.85rem;'
        f'color:rgba(255,255,255,0.7);font-family:monospace;">🔍 {q}</div>',
        unsafe_allow_html=True,
    )

# ─── Market Articles ────────────────────────────────────────────
st.markdown("### 📰 Market Articles")
sample_articles = [
    {
        "title": f"{st.session_state.get('industry', 'AI')} Market Expected to Reach $500B by 2030",
        "source": "Market Research Today",
        "date": "2026-07-28",
        "summary": f"The global {st.session_state.get('industry', 'AI')} market is projected to grow at a CAGR of 22.4%, driven by increasing adoption across enterprises and SMEs. Key growth factors include digital transformation initiatives and rising demand for automation.",
        "relevance": 0.95,
        "url": "#",
    },
    {
        "title": f"Top 10 {st.session_state.get('industry', 'Startup')} Startups to Watch in 2026",
        "source": "TechCrunch",
        "date": "2026-07-25",
        "summary": "Emerging startups in this space are attracting significant venture capital funding. The competitive landscape is evolving rapidly with new entrants focusing on niche segments.",
        "relevance": 0.88,
        "url": "#",
    },
    {
        "title": f"How AI is Transforming the {st.session_state.get('industry', 'Technology')} Industry",
        "source": "Forbes",
        "date": "2026-07-20",
        "summary": "Artificial intelligence is reshaping traditional business models. Companies that leverage AI for personalization and efficiency are gaining competitive advantages.",
        "relevance": 0.82,
        "url": "#",
    },
]
for article in sample_articles:
    render_article_card(article)

# ─── Competitor URLs ────────────────────────────────────────────
st.markdown("### 🏢 Competitor URLs Discovered")
competitors = [
    {"name": "CompetitorAlpha", "url": "https://competitoralpha.com", "relevance": "High"},
    {"name": "MarketLeader Inc", "url": "https://marketleader.io", "relevance": "High"},
    {"name": "StartupBeta", "url": "https://startupbeta.co", "relevance": "Medium"},
    {"name": "NextGen Solutions", "url": "https://nextgen.solutions", "relevance": "Medium"},
    {"name": "InnovateTech", "url": "https://innovatetech.ai", "relevance": "Low"},
]
for comp in competitors:
    st.markdown(
        f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
        f'border-radius:8px;padding:0.5rem 0.75rem;margin-bottom:0.3rem;display:flex;'
        f'justify-content:space-between;align-items:center;">'
        f'<span style="font-size:0.9rem;">🔗 {comp["name"]}</span>'
        f'<span style="font-size:0.8rem;color:#4d94ff;">{comp["url"]}</span>'
        f'<span class="status-badge {"success" if comp["relevance"] == "High" else "warning" if comp["relevance"] == "Medium" else "info"}">'
        f'{comp["relevance"]}</span></div>',
        unsafe_allow_html=True,
    )

# ─── Funding News ───────────────────────────────────────────────
st.markdown("### 💰 Recent Funding News")
funding_items = [
    {"company": "TechVenture AI", "amount": "$45M Series B", "date": "July 2026", "investors": "Sequoia, Accel"},
    {"company": "DataFlow Inc", "amount": "$22M Series A", "date": "June 2026", "investors": "Andreessen Horowitz"},
    {"company": "SmartAnalytics", "amount": "$10M Seed", "date": "May 2026", "investors": "YC, AngelList"},
]
for item in funding_items:
    st.markdown(
        f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
        f'border-radius:10px;padding:1rem;margin-bottom:0.5rem;">'
        f'<div style="display:flex;justify-content:space-between;align-items:center;">'
        f'<div><span style="font-weight:600;">{item["company"]}</span>'
        f'<span style="font-size:0.8rem;color:rgba(255,255,255,0.5);margin-left:0.75rem;">{item["date"]}</span></div>'
        f'<span style="font-weight:700;color:#00d4aa;">{item["amount"]}</span></div>'
        f'<div style="font-size:0.8rem;color:rgba(255,255,255,0.4);margin-top:0.25rem;">'
        f'Investors: {item["investors"]}</div></div>',
        unsafe_allow_html=True,
    )

# ─── Source Confidence ──────────────────────────────────────────
st.markdown("### 📊 Source Confidence Scores")
sources = [
    ("TechCrunch", 92, "success"),
    ("Crunchbase", 88, "success"),
    ("Google News", 85, "success"),
    ("LinkedIn", 78, "success"),
    ("Reddit", 65, "warning"),
    ("Twitter/X", 55, "warning"),
]
for name, score, badge in sources:
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:1rem;padding:0.5rem 0;'
        f'border-bottom:1px solid rgba(255,255,255,0.05);">'
        f'<span style="font-size:0.9rem;flex:1;">{name}</span>'
        f'<div style="width:150px;height:6px;background:rgba(255,255,255,0.1);border-radius:3px;">'
        f'<div style="width:{score}%;height:100%;background:{"#00d4aa" if score >= 80 else "#ffd93d" if score >= 60 else "#ff6b6b"};'
        f'border-radius:3px;"></div></div>'
        f'<span style="font-size:0.8rem;font-weight:600;color:{"#00d4aa" if score >= 80 else "#ffd93d" if score >= 60 else "#ff6b6b"};'
        f'width:35px;text-align:right;">{score}%</span></div>',
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
    if st.button("🏆 Competitor Analysis →", use_container_width=True):
        st.switch_page("pages/04_Competitor_Analysis.py")
with col3:
    if st.button("📄 Final Report →", use_container_width=True):
        st.switch_page("pages/08_Final_Report.py")

render_footer()