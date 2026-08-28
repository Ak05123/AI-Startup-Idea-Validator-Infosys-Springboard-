"""
MVP Recommendation Page - Displays results from agents/mvp_recommendation_agent.py.
No analysis logic - only displays backend results.
"""

import streamlit as st

st.set_page_config(page_title="MVP Recommendation - AI Startup Idea Validator", page_icon="💡", layout="wide", initial_sidebar_state="collapsed")

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.session_state import init_session_state, has_startup_idea
init_session_state()
from components.hero_section import render_page_header, render_startup_info_header
from components.footer import render_footer
from components.report_cards import render_feature_item
from components.charts import create_timeline_gantt

if not has_startup_idea():
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_page_header("💡", "MVP Recommendation", "Minimum Viable Product strategy and development roadmap", "Home > MVP Recommendation")
render_startup_info_header()

# ─── Cost Overview ──────────────────────────────────────────────
st.markdown("### 💰 Cost Overview")
col1, col2, col3, col4 = st.columns(4)
costs = [("Development", "$150K-$200K", "#4d94ff"), ("Infrastructure", "$5K-$10K/mo", "#00d4aa"), ("API Costs", "$2K-$5K/mo", "#ffd93d"), ("Team Size", "5-7 People", "#ff6b6b")]
for i, (label, value, color) in enumerate(costs):
    with [col1, col2, col3, col4][i]:
        st.markdown(
            f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);'
            f'border:1px solid rgba(255,255,255,0.08);border-radius:12px;">'
            f'<div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{label}</div>'
            f'<div style="font-size:1.3rem;font-weight:700;color:{color};margin-top:0.25rem;">{value}</div></div>',
            unsafe_allow_html=True,
        )

# ─── Core Features ──────────────────────────────────────────────
st.markdown("### 🎯 Core Features (Prioritized)")
features = [
    {"feature": "AI-Powered Search Agent", "priority": "P0", "complexity": "High", "impact": 5},
    {"feature": "Market Analysis Dashboard", "priority": "P0", "complexity": "High", "impact": 5},
    {"feature": "Competitor Intelligence Module", "priority": "P0", "complexity": "Medium", "impact": 4},
    {"feature": "SWOT Analysis Generator", "priority": "P1", "complexity": "Medium", "impact": 4},
    {"feature": "MVP Recommendation Engine", "priority": "P1", "complexity": "High", "impact": 4},
    {"feature": "GTM Strategy Builder", "priority": "P1", "complexity": "Medium", "impact": 3},
    {"feature": "Report Generator (PDF/MD/JSON)", "priority": "P2", "complexity": "Low", "impact": 3},
    {"feature": "AI Conversational Advisor", "priority": "P2", "complexity": "Medium", "impact": 3},
]
for feat in features:
    render_feature_item(feat)

# ─── Development Timeline ───────────────────────────────────────
st.markdown("### 📅 Development Timeline")
phases = [
    {"name": "Foundation", "duration": 4},
    {"name": "Core AI Engine", "duration": 6},
    {"name": "Dashboard & UI", "duration": 4},
    {"name": "Integration & Testing", "duration": 3},
]
fig = create_timeline_gantt(phases)
st.plotly_chart(fig, use_container_width=True)

# ─── Technology Suggestions ─────────────────────────────────────
st.markdown("### 🛠️ Technology Stack")
tech_stack = [
    ("Frontend", "Streamlit, React, TypeScript", "🎨"),
    ("Backend", "Python, FastAPI, LangChain", "⚙️"),
    ("AI/ML", "OpenAI GPT-4, LangChain Agents", "🧠"),
    ("Database", "PostgreSQL, Redis, Pinecone", "🗄️"),
    ("Infrastructure", "Azure, Docker, Kubernetes", "☁️"),
    ("Monitoring", "Application Insights, Log Analytics", "📊"),
]
cols = st.columns(3)
for i, (layer, tech, icon) in enumerate(tech_stack):
    with cols[i % 3]:
        st.markdown(
            f'<div style="background:rgba(77,148,255,0.05);border:1px solid rgba(77,148,255,0.12);'
            f'border-radius:12px;padding:1.25rem;text-align:center;height:100%;">'
            f'<div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div>'
            f'<div style="font-weight:600;font-size:0.85rem;margin-bottom:0.25rem;">{layer}</div>'
            f'<div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{tech}</div></div>',
            unsafe_allow_html=True,
        )

# ─── Navigation ─────────────────────────────────────────────────
st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)
st.markdown("### ▶️ Continue Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📢 GTM Strategy →", use_container_width=True):
        st.switch_page("pages/07_GTM.py")
with col2:
    if st.button("📄 Final Report →", use_container_width=True):
        st.switch_page("pages/08_Final_Report.py")
with col3:
    if st.button("🤖 AI Advisor →", use_container_width=True):
        st.switch_page("pages/09_AI_Advisor.py")

render_footer()