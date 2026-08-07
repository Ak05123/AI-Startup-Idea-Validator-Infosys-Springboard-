"""
Home Page - Premium landing page with hero section and startup validation form.
Integrates with backend app/orchestrator.py for AI processing.
"""

import streamlit as st

st.set_page_config(
    page_title="Home - AI Startup Idea Validator",
    page_icon="🚀",
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

from components.hero_section import render_hero_section
from components.footer import render_footer

# ─── Hero Section ───────────────────────────────────────────────
render_hero_section()

# ─── Startup Validation Form ────────────────────────────────────
st.markdown(
    """
    <div style="text-align:center;margin:1.5rem 0 1rem;">
        <h2 style="font-size:1.5rem;font-weight:700;">📋 Validate Your Startup Idea</h2>
        <p style="font-size:0.9rem;color:rgba(255,255,255,0.5);">
            Fill in the details below to get a comprehensive AI-powered validation report
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Center the form with a max-width container
st.markdown(
    """
    <style>
        .centered-form {
            max-width: 720px;
            margin: 0 auto;
            background: rgba(255,255,255,0.03);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        .centered-form .stTextInput > div > div,
        .centered-form .stTextArea > div > div,
        .centered-form .stSelectbox > div > div,
        .centered-form .stNumberInput > div > div {
            background: rgba(255,255,255,0.05) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 8px !important;
        }
        .centered-form .stTextInput > div > div:hover,
        .centered-form .stTextArea > div > div:hover,
        .centered-form .stSelectbox > div > div:hover,
        .centered-form .stNumberInput > div > div:hover {
            border-color: #0066ff !important;
        }
        .centered-form .stTextInput input,
        .centered-form .stTextArea textarea {
            color: #ffffff !important;
            font-family: 'Inter', sans-serif !important;
        }
        .centered-form .stButton > button {
            background: linear-gradient(135deg, #0066ff 0%, #00d4aa 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 102, 255, 0.3);
            width: 100%;
        }
        .centered-form .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 102, 255, 0.4);
        }
        @media (max-width: 768px) {
            .centered-form {
                padding: 1.5rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="centered-form">', unsafe_allow_html=True)

# Startup Idea (Required)
startup_idea = st.text_area(
    "Startup Idea *",
    value=st.session_state.get("startup_idea", ""),
    placeholder="Describe your startup idea in detail...\n\nExample: An AI platform that helps students prepare for technical interviews using personalized learning paths and mock interviews.",
    height=150,
    key="input_startup_idea",
)

# Industry
industry = st.selectbox(
    "Industry",
    ["", "EdTech", "Healthcare", "FinTech", "Agriculture", "Retail",
     "AI & ML", "Cybersecurity", "SaaS", "Transportation", "Energy",
     "E-commerce", "Entertainment", "Real Estate", "Other"],
    index=0 if not st.session_state.get("industry") else (
        ["", "EdTech", "Healthcare", "FinTech", "Agriculture", "Retail",
         "AI & ML", "Cybersecurity", "SaaS", "Transportation", "Energy",
         "E-commerce", "Entertainment", "Real Estate", "Other"].index(st.session_state["industry"])
    ),
    key="input_industry",
)

# Country
country = st.selectbox(
    "Country",
    ["", "United States", "India", "United Kingdom", "Canada", "Australia",
     "Germany", "France", "Singapore", "UAE", "Brazil", "Japan", "Other"],
    index=0 if not st.session_state.get("country") else (
        ["", "United States", "India", "United Kingdom", "Canada", "Australia",
         "Germany", "France", "Singapore", "UAE", "Brazil", "Japan", "Other"].index(st.session_state["country"])
    ),
    key="input_country",
)

# Budget
budget = st.number_input(
    "Budget ($)",
    min_value=0,
    max_value=10000000,
    value=st.session_state.get("budget", 0),
    step=1000,
    format="%d",
    key="input_budget",
)

# Keywords
keywords_input = st.text_input(
    "Keywords (comma-separated)",
    value=", ".join(st.session_state.get("keywords", [])),
    placeholder="e.g., AI, education, interview prep, machine learning",
    key="input_keywords",
)

st.markdown('</div>', unsafe_allow_html=True)

# ─── Validate Button ────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Validate Startup Idea", use_container_width=True, type="primary"):
        if not startup_idea.strip():
            st.warning("Please enter your startup idea.")
        else:
            # Store in session state
            st.session_state["startup_idea"] = startup_idea.strip()
            st.session_state["industry"] = industry
            st.session_state["country"] = country
            st.session_state["budget"] = budget
            st.session_state["keywords"] = [k.strip() for k in keywords_input.split(",") if k.strip()]
            st.session_state["form_validated"] = True
            st.session_state["pipeline_status"] = "running"
            st.switch_page("pages/02_Web_Search.py")

# ─── Features Section ───────────────────────────────────────────
st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center;margin:2rem 0 1rem;">
        <h2 style="font-size:1.5rem;font-weight:700;">🚀 Powered by Multi-Agent AI Intelligence</h2>
        <p style="font-size:0.9rem;color:rgba(255,255,255,0.5);">
            Nine specialized AI agents work together to validate your startup idea
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

features = [
    ("🌐", "Web Search Agent", "Scrapes real-time market data, news, and competitor information from across the web"),
    ("📈", "Market Analysis Agent", "Analyzes market size, growth trends, customer segments, and future opportunities"),
    ("🏆", "Competitor Agent", "Identifies direct and indirect competitors with pricing, strengths, and market position"),
    ("⚠️", "SWOT & Risk Agent", "Evaluates strengths, weaknesses, opportunities, threats, and business risks"),
    ("💡", "MVP Agent", "Recommends priority features, development timeline, and technology stack"),
    ("📢", "GTM Strategy Agent", "Creates go-to-market plan with pricing, channels, and launch strategy"),
    ("📄", "Report Agent", "Generates comprehensive executive summary with scores and recommendations"),
    ("🤖", "AI Advisor", "Conversational AI assistant for answering questions about your startup"),
]

cols = st.columns(4)
for i, (icon, title, desc) in enumerate(features):
    with cols[i % 4]:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ─── Footer ─────────────────────────────────────────────────────
st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)
render_footer()