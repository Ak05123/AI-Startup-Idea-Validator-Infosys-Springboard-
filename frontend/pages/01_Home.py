"""
AI Startup Idea Validator - Home Page
Clean landing page with hero section and startup validation form.
"""
import streamlit as st
from components.footer import render_footer

st.set_page_config(page_title="Home", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.helpers import init_session_state
init_session_state()

# Hero Section
st.markdown(
    """
    <div style="text-align:center;padding:3.5rem 2rem;margin-bottom:1.5rem;
        background:linear-gradient(135deg,#0a0a1a 0%,#1a1a3e 50%,#0a0a1a 100%);
        border-radius:16px;position:relative;overflow:hidden;">
        <div style="position:absolute;top:0;left:0;right:0;bottom:0;
            background:radial-gradient(circle at 50% 50%,rgba(0,102,255,0.15) 0%,transparent 50%);pointer-events:none;"></div>
        <div style="position:relative;z-index:1;">
            <div style="font-size:3.5rem;margin-bottom:1rem;">🚀</div>
            <h1 style="font-size:3rem;font-weight:800;
                background:linear-gradient(135deg,#fff 0%,#4d94ff 50%,#00d4aa 100%);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
                margin-bottom:0.75rem;line-height:1.2;">AI Startup Idea Validator</h1>
            <p style="font-size:1.15rem;color:rgba(255,255,255,0.7);max-width:600px;margin:0 auto 1.5rem;line-height:1.6;">
                Validate startup ideas using AI-powered Multi-Agent Intelligence. Make data-driven decisions with comprehensive market analysis.</p>
            <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;max-width:800px;margin:2rem auto 0;">
                <div style="padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;">
                    <div style="font-size:2rem;font-weight:700;color:#4d94ff;">10+</div>
                    <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Sources Analyzed</div>
                </div>
                <div style="padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;">
                    <div style="font-size:2rem;font-weight:700;color:#4d94ff;">87%</div>
                    <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Confidence Score</div>
                </div>
                <div style="padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;">
                    <div style="font-size:2rem;font-weight:700;color:#4d94ff;">3s</div>
                    <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Analysis Time</div>
                </div>
                <div style="padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;">
                    <div style="font-size:2rem;font-weight:700;color:#4d94ff;">9</div>
                    <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">AI Agents</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Startup Validation Form
st.markdown("""
<div style="text-align:center;margin:1.5rem 0 1rem;">
    <h2 style="font-size:1.5rem;font-weight:700;">📋 Validate Your Startup Idea</h2>
    <p style="font-size:0.9rem;color:rgba(255,255,255,0.5);">Fill in the details below to get a comprehensive AI-powered validation report</p>
</div>
""", unsafe_allow_html=True)

# Center the form with a max-width container
st.markdown("""
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
""", unsafe_allow_html=True)

st.markdown('<div class="centered-form">', unsafe_allow_html=True)

# Startup Idea (Required)
startup_idea = st.text_area(
    "Startup Idea *",
    value=st.session_state.get("startup_idea", ""),
    placeholder="Example:\nAn AI platform that helps students prepare for technical interviews using personalized learning paths and mock interviews.",
    height=150,
    key="input_startup_idea"
)

# Industry
industry = st.selectbox(
    "Industry",
    ["", "EdTech", "Healthcare", "FinTech", "Agriculture", "Retail", "AI", "Cybersecurity", "SaaS", "Transportation", "Energy"],
    index=0 if not st.session_state.get("industry") else ["", "EdTech", "Healthcare", "FinTech", "Agriculture", "Retail", "AI", "Cybersecurity", "SaaS", "Transportation", "Energy"].index(st.session_state["industry"]),
    key="input_industry"
)

# Country
country = st.selectbox(
    "Country",
    ["", "United States", "India", "United Kingdom", "Canada", "Australia", "Germany", "France", "Singapore", "UAE", "Brazil", "Japan", "Other"],
    index=0 if not st.session_state.get("country") else ["", "United States", "India", "United Kingdom", "Canada", "Australia", "Germany", "France", "Singapore", "UAE", "Brazil", "Japan", "Other"].index(st.session_state["country"]),
    key="input_country"
)

# Budget
budget = st.number_input(
    "Budget ($)",
    min_value=0,
    max_value=10000000,
    value=st.session_state.get("budget", 0),
    step=1000,
    format="%d",
    key="input_budget"
)

# Keywords
keywords_input = st.text_input(
    "Keywords (comma-separated)",
    value=", ".join(st.session_state.get("keywords", [])),
    placeholder="e.g., AI, education, interview prep",
    key="input_keywords"
)

st.markdown('</div>', unsafe_allow_html=True)

# Validate and Submit
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
            st.switch_page("pages/02_Web_Search_Agent.py")

st.markdown('<hr style="border-color:rgba(255,255,255,0.08);margin:2rem 0;">', unsafe_allow_html=True)
render_footer()