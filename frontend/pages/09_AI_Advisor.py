"""AI Advisor - ChatGPT-like chat interface for startup advice."""
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
from utils.page_utils import render_breadcrumb, render_hero, render_section, render_faqs, render_summary, render_page_footer
import time, random

render_breadcrumb("🤖 AI Advisor")
render_hero("🤖", "AI Advisor", "Your personal AI startup advisor — ask anything about your idea", "The AI Advisor is a conversational interface that provides personalized guidance about your startup. Ask questions about market analysis, competitors, strategy, or any aspect of your business. Backend-ready for future LLM integration.")

MOCK_RESPONSES = [
    "Based on my analysis of your startup idea, I see strong potential in the market. The key factors to consider are:\n\n1. **Market Size**: The TAM is projected at $8.5B by 2028\n2. **Competition**: There are 5 major competitors, but your AI-native approach gives you an edge\n3. **Timing**: Market conditions are favorable for entry right now\n\nWould you like me to dive deeper into any of these areas?",
    "Great question! Here are my recommendations for your MVP:\n\n• **Core Feature**: Focus on the AI-powered search agent first (P0 priority)\n• **Timeline**: 6 weeks for initial development\n• **Team**: 5-7 engineers recommended\n• **Budget**: $150K - $200K initial investment\n\nRemember: Start with the most impactful features and iterate based on user feedback.",
    "Looking at the competitive landscape, here's what I've found:\n\n**Key Insights:**\n1. PitchBook and CB Insights dominate with 50% combined market share\n2. Your advantage lies in AI-native architecture vs their legacy systems\n3. The SME segment is underserved by current players\n\n**Recommendation:** Target SMEs first with a freemium model to build traction.",
    "Let me analyze the risks for your startup:\n\n**High Priority Risks:**\n• Competition from established players (80% probability)\n• Data reliability challenges (50% probability)\n\n**Mitigation Strategies:**\n1. Focus on AI-native features they can't easily replicate\n2. Implement multi-source verification\n3. Build strong data partnerships early\n\nWould you like me to elaborate on any of these risks?",
    "Here's my analysis of the market trends:\n\n**Current Trends:**\n1. AI adoption in enterprises reached 72% in 2026\n2. Multi-agent AI systems are transforming business intelligence\n3. Automated validation reduces research time by 80%\n\n**Opportunity:** The market is growing at 22.4% CAGR, making this an excellent time to enter.",
    "For your GTM strategy, I recommend:\n\n**Launch Timeline:**\n• Pre-launch (4 weeks): Build community, create content\n• Launch (2 weeks): Product Hunt, TechCrunch, LinkedIn\n• Post-launch (8 weeks): Iterate based on feedback\n\n**Pricing Strategy:**\n• Starter: $49/month (5 validations)\n• Professional: $149/month (25 validations)\n• Enterprise: Custom pricing\n\nStart with Professional tier as your primary offering.",
    "Excellent progress! Here's what I suggest for your next steps:\n\n1. **Week 1-2**: Finalize your MVP feature set\n2. **Week 3-4**: Build core AI search agent\n3. **Week 5-6**: Add market analysis dashboard\n4. **Week 7-8**: Implement competitor tracking\n5. **Week 9-10**: Launch beta to 100 users\n\nRemember: Validate early, iterate often!",
    "I've analyzed your funding strategy. Here are my insights:\n\n**Recommended Approach:**\n1. Start with angel/seed round of $500K-$1M\n2. Focus on building traction with 100+ beta users\n3. Target Series A after 12-18 months with $3-5M\n\n**Key Metrics Investors Look For:**\n• Monthly active users\n• Revenue growth rate\n• Customer acquisition cost\n• Net promoter score\n\nWould you like me to help you prepare a pitch deck?",
]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if not st.session_state.chat_history:
    st.session_state.chat_history.append({"role": "assistant", "content": "👋 Hello! I'm your AI Startup Advisor. I can help you with:\n\n• **Market Analysis** — Understand your market size and trends\n• **Competitor Research** — Analyze your competitive landscape\n• **SWOT Analysis** — Identify strengths, weaknesses, opportunities, and threats\n• **MVP Planning** — Get recommendations for your minimum viable product\n• **GTM Strategy** — Plan your go-to-market approach\n• **Risk Assessment** — Identify and mitigate potential risks\n\nWhat would you like to discuss about your startup idea?"})

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
quick_qs = [("📊 Market Size", "What is the market size for AI validation tools?"), ("🏆 Competitors", "Who are my main competitors?"), ("⚠️ Key Risks", "What are the biggest risks?"), ("💡 MVP Advice", "What should my MVP include?")]
for i, (label, question) in enumerate(quick_qs):
    with [col1, col2, col3, col4][i]:
        if st.button(label, use_container_width=True, key=f"quick_{i}"):
            st.session_state.chat_history.append({"role": "user", "content": question})
            with st.spinner("🤖 Thinking..."):
                time.sleep(1.5)
                st.session_state.chat_history.append({"role": "assistant", "content": random.choice(MOCK_RESPONSES)})
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
            time.sleep(random.uniform(1.0, 2.5))
            st.session_state.chat_history.append({"role": "assistant", "content": random.choice(MOCK_RESPONSES)})
        st.rerun()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

render_section("🔍 What is AI Advisor?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p>The <strong>AI Advisor</strong> is a conversational AI interface that provides personalized startup guidance. It can answer questions about market analysis, competitors, strategy, and more. The system is designed to connect to any LLM backend (OpenAI, Anthropic, open-source models) for real intelligence.</p></div>""", unsafe_allow_html=True)

render_section("🎯 Why is it Important?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Instant Answers:</strong> Get immediate responses to your startup questions.</p><p><strong>Personalized Guidance:</strong> Advice tailored to your specific startup context.</p><p><strong>24/7 Availability:</strong> Access expert advice anytime, anywhere.</p><p><strong>Cost Effective:</strong> Free alternative to expensive consultants.</p><p><strong>Backend Ready:</strong> Seamless integration with real AI models.</p></div>""", unsafe_allow_html=True)

render_faqs([("How does the AI Advisor work?", "The AI Advisor uses natural language processing to understand your questions and generate relevant responses. Currently using mock responses, it's designed to connect to any LLM backend."), ("What can I ask about?", "You can ask about market analysis, competitors, SWOT, MVP planning, GTM strategy, risks, funding, and any other startup-related topics."), ("Is my conversation private?", "Yes! Chat history is stored only in your session and is cleared when you close the browser."), ("When will real AI be integrated?", "The backend integration layer is ready. Real AI models can be connected by configuring the API endpoint in settings."), ("Can I export chat history?", "Chat history export will be available in a future update."), ("How are responses generated?", "Currently using curated mock responses that cover common startup questions. Real AI integration will provide dynamic, context-aware responses.")])
render_summary("📋 Summary", "The AI Advisor provides conversational startup guidance with a ChatGPT-like interface. It's designed to be backend-ready for future LLM integration, with mock responses providing immediate value. Ask anything about your startup idea and get personalized, actionable advice.")
render_page_footer()