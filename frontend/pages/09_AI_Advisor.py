"""AI Advisor - Chat interface that sends questions to the backend conversational_advisor.py."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="AI Advisor", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()
from utils.page_utils import render_breadcrumb, render_section, render_page_footer
from utils.backend_client import ask_advisor

render_breadcrumb("🤖 AI Advisor")

startup_idea = st.session_state.get("startup_idea", "")

if not startup_idea:
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if not st.session_state.chat_history:
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": "👋 Hello! I'm your AI Startup Advisor. I can help you with:\n\n• **Market Analysis** — Understand your market size and trends\n• **Competitor Research** — Analyze your competitive landscape\n• **SWOT Analysis** — Identify strengths, weaknesses, opportunities, and threats\n• **MVP Planning** — Get recommendations for your minimum viable product\n• **GTM Strategy** — Plan your go-to-market approach\n• **Risk Assessment** — Identify and mitigate potential risks\n\nWhat would you like to discuss about your startup idea?"
    })

# Chat display
st.markdown('<div style="max-width:800px;margin:0 auto;">', unsafe_allow_html=True)
for message in st.session_state.chat_history:
    role = message["role"]
    content = message["content"]
    if role == "assistant":
        st.markdown(f'<div style="display:flex;gap:0.75rem;margin-bottom:1rem;animation:fadeIn 0.3s ease;"><div style="width:2.5rem;height:2.5rem;border-radius:50%;background:linear-gradient(135deg,#0066ff,#00d4aa);display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0;">🤖</div><div style="max-width:70%;padding:0.75rem 1rem;border-radius:12px;border-bottom-left-radius:4px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);font-size:0.9rem;line-height:1.6;color:rgba(255,255,255,0.8);">{content}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="display:flex;gap:0.75rem;margin-bottom:1rem;flex-direction:row-reverse;animation:fadeIn 0.3s ease;"><div style="width:2.5rem;height:2.5rem;border-radius:50%;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0;">👤</div><div style="max-width:70%;padding:0.75rem 1rem;border-radius:12px;border-bottom-right-radius:4px;background:linear-gradient(135deg,#0066ff,#0052cc);color:white;font-size:0.9rem;line-height:1.6;">{content}</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Quick questions
st.markdown('<div style="margin:1rem 0;"><div style="font-size:0.85rem;color:rgba(255,255,255,0.5);margin-bottom:0.5rem;">Quick Questions:</div></div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
quick_qs = [("📊 Market Size", "What is the market size for this idea?"), ("🏆 Competitors", "Who are my main competitors?"), ("⚠️ Key Risks", "What are the biggest risks?"), ("💡 MVP Advice", "What should my MVP include?")]
for i, (label, question) in enumerate(quick_qs):
    with [col1, col2, col3, col4][i]:
        if st.button(label, use_container_width=True, key=f"quick_{i}"):
            st.session_state.chat_history.append({"role": "user", "content": question})
            with st.spinner("🤖 Thinking..."):
                context = {
                    "startup_idea": st.session_state.get("startup_idea", ""),
                    "industry": st.session_state.get("industry", ""),
                    "country": st.session_state.get("country", ""),
                    "keywords": st.session_state.get("keywords", []),
                    "backend_response": st.session_state.get("backend_response"),
                }
                result = ask_advisor(question, context)
                if result["status"] == "success":
                    response = result["response"]
                else:
                    response = f"⚠️ {result['response']}"
                st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.rerun()

# Chat input
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input("Message", placeholder="Type your question here...", label_visibility="collapsed")
    with col2:
        submit = st.form_submit_button("Send 📤", use_container_width=True)
    if submit and user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("🤖 Thinking..."):
            context = {
                "startup_idea": st.session_state.get("startup_idea", ""),
                "industry": st.session_state.get("industry", ""),
                "country": st.session_state.get("country", ""),
                "keywords": st.session_state.get("keywords", []),
                "backend_response": st.session_state.get("backend_response"),
            }
            result = ask_advisor(user_input, context)
            if result["status"] == "success":
                response = result["response"]
            else:
                response = f"⚠️ {result['response']}"
            st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

render_page_footer()