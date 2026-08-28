"""
GTM Strategy Page - Displays results from agents/gtm_strategy_agent.py.
No analysis logic - only displays backend results.
"""

import streamlit as st

st.set_page_config(page_title="GTM Strategy - AI Startup Idea Validator", page_icon="📢", layout="wide", initial_sidebar_state="collapsed")

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.session_state import init_session_state, has_startup_idea
init_session_state()
from components.hero_section import render_page_header, render_startup_info_header
from components.footer import render_footer
from components.report_cards import render_pricing_tier

if not has_startup_idea():
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_page_header("📢", "Go-To-Market Strategy", "Launch plan, pricing, and customer acquisition strategy", "Home > GTM Strategy")
render_startup_info_header()

# ─── Launch Timeline ────────────────────────────────────────────
st.markdown("### 📅 Launch Timeline")
phases = [
    ("🔧", "Pre-Launch", "4 Weeks", "#ffd93d"),
    ("🚀", "Launch", "2 Weeks", "#00d4aa"),
    ("📈", "Post-Launch", "8 Weeks", "#4d94ff"),
    ("🌱", "Scale", "Ongoing", "#0066ff"),
]
cols = st.columns(4)
for i, (icon, phase, duration, color) in enumerate(phases):
    with cols[i]:
        st.markdown(
            f'<div class="timeline-phase" style="border-top:4px solid {color};">'
            f'<div style="font-size:2rem;margin-bottom:0.25rem;">{icon}</div>'
            f'<div style="font-size:0.95rem;font-weight:600;text-transform:capitalize;">{phase}</div>'
            f'<div style="font-size:0.85rem;color:{color};font-weight:500;margin-top:0.25rem;">{duration}</div></div>',
            unsafe_allow_html=True,
        )

# ─── Pricing Strategy ───────────────────────────────────────────
st.markdown("### 💰 Pricing Strategy")
pricing_tiers = [
    {"tier": "Starter", "icon": "🌱", "price": "$49/mo", "features": ["5 validations/mo", "Basic market analysis", "Email support", "Standard reports"]},
    {"tier": "Professional", "icon": "⭐", "price": "$149/mo", "features": ["25 validations/mo", "Advanced market analysis", "Priority support", "Custom reports", "API access"]},
    {"tier": "Enterprise", "icon": "👑", "price": "$499/mo", "features": ["Unlimited validations", "Full agent suite", "Dedicated support", "Custom integrations", "SLA guarantee", "Team collaboration"]},
]
cols = st.columns(3)
for i, tier in enumerate(pricing_tiers):
    with cols[i]:
        render_pricing_tier(tier, ["#4d94ff", "#0066ff", "#00d4aa"][i], featured=(i == 1))

# ─── Target Customers ───────────────────────────────────────────
st.markdown("### 🎯 Target Customers")
segments = [
    ("🚀", "Startup Founders", "Early-stage founders validating their business ideas before building"),
    ("💼", "Entrepreneurs", "Serial entrepreneurs evaluating multiple business opportunities"),
    ("🏢", "SME Owners", "Small business owners exploring new market opportunities"),
    ("🎓", "Students", "Student entrepreneurs in incubators and accelerator programs"),
    ("💰", "Investors", "Angel investors and VCs evaluating startup investment opportunities"),
]
cols = st.columns(3)
for i, (icon, title, desc) in enumerate(segments):
    with cols[i % 3]:
        st.markdown(
            f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
            f'border-radius:12px;padding:1.25rem;text-align:center;height:100%;">'
            f'<div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div>'
            f'<div style="font-weight:600;font-size:0.85rem;margin-bottom:0.25rem;">{title}</div>'
            f'<div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{desc}</div></div>',
            unsafe_allow_html=True,
        )

# ─── Marketing Channels ─────────────────────────────────────────
st.markdown("### 📡 Marketing Channels")
channels = [
    ("🚀", "Product Hunt", "Launch on Product Hunt for initial traction"),
    ("📰", "TechCrunch/Forbes", "PR outreach for media coverage"),
    ("💼", "LinkedIn", "B2B marketing and thought leadership"),
    ("🎓", "Startup Communities", "Engage on Indie Hackers, Hacker News"),
    ("💬", "Social Media", "Twitter/X, Reddit communities"),
    ("📝", "Content Marketing", "Blog posts, case studies, whitepapers"),
]
cols = st.columns(3)
for i, (icon, channel, desc) in enumerate(channels):
    with cols[i % 3]:
        st.markdown(
            f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);'
            f'border:1px solid rgba(255,255,255,0.08);border-radius:12px;height:100%;">'
            f'<div style="font-size:2rem;margin-bottom:0.25rem;">{icon}</div>'
            f'<div style="font-weight:600;font-size:0.9rem;">{channel}</div>'
            f'<div style="font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:0.25rem;">{desc}</div></div>',
            unsafe_allow_html=True,
        )

# ─── Customer Acquisition Strategy ──────────────────────────────
st.markdown("### 📈 Customer Acquisition Strategy")
strategies = [
    ("🌱", "Product-Led Growth", "Free tier drives adoption and word-of-mouth referrals"),
    ("🤝", "Community Building", "Engage startup communities on Product Hunt, HN, Reddit, Indie Hackers"),
    ("📝", "Content Marketing", "Publish market research reports and startup validation case studies"),
    ("🤝", "Partnership Program", "Partner with accelerators, VCs, and startup incubators"),
    ("🎯", "Targeted Ads", "LinkedIn and Google Ads targeting founders and entrepreneurs"),
    ("📧", "Email Marketing", "Drip campaigns for free trial users and newsletter subscribers"),
]
cols = st.columns(2)
for i, (icon, title, desc) in enumerate(strategies):
    with cols[i % 2]:
        st.markdown(
            f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
            f'border-radius:10px;padding:1rem;margin-bottom:0.5rem;">'
            f'<div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.25rem;">'
            f'<span style="font-size:1.5rem;">{icon}</span>'
            f'<span style="font-weight:600;font-size:0.9rem;">{title}</span></div>'
            f'<div style="font-size:0.85rem;color:rgba(255,255,255,0.5);">{desc}</div></div>',
            unsafe_allow_html=True,
        )

# ─── Navigation ─────────────────────────────────────────────────
st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)
st.markdown("### ▶️ Continue Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📄 Final Report →", use_container_width=True):
        st.switch_page("pages/08_Final_Report.py")
with col2:
    if st.button("🤖 AI Advisor →", use_container_width=True):
        st.switch_page("pages/09_AI_Advisor.py")
with col3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")

render_footer()