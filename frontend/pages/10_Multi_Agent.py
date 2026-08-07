"""Multi-Agent AI Architecture - Detailed explanation of the multi-agent system."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Multi-Agent AI", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()
from utils.page_utils import render_breadcrumb, render_hero, render_section, render_card, render_workflow, render_tech_badges, render_table, render_advantages, render_challenges, render_faqs, render_summary, render_page_footer, navigate_to

render_breadcrumb("🤖 Multi-Agent AI")
render_hero("🤖", "Multi-Agent AI Architecture", "A system of specialized AI agents working together for comprehensive startup validation", "Our platform uses a multi-agent architecture where each AI agent has a specific responsibility. The Orchestrator Agent coordinates all agents, passing data between them to produce a complete validation pipeline. This modular design allows each agent to be developed, tested, and improved independently.")

render_section("🔍 What is Multi-Agent AI?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Multi-Agent AI</strong> is an architecture where multiple specialized AI agents work together to solve complex problems. Each agent has a specific role and expertise, and they communicate through a central orchestrator. This approach is more powerful than a single monolithic AI because each agent can be optimized for its specific task.</p></div>""", unsafe_allow_html=True)

render_section("🎯 Why is it Important?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Modularity:</strong> Each agent is independent and can be updated separately.</p><p><strong>Specialization:</strong> Agents become experts in their specific domain.</p><p><strong>Scalability:</strong> New agents can be added without affecting existing ones.</p><p><strong>Fault Tolerance:</strong> If one agent fails, others continue functioning.</p><p><strong>Parallel Processing:</strong> Multiple agents can work simultaneously.</p></div>""", unsafe_allow_html=True)

# Architecture Diagram
render_section("🏗️ System Architecture")
st.markdown("""<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:2rem;margin:1rem 0;"><div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;"><div style="background:linear-gradient(135deg,#0066ff,#00d4aa);padding:0.75rem 2rem;border-radius:10px;font-weight:700;">👤 User Input</div><div style="color:rgba(0,102,255,0.4);font-size:1.2rem;">↓</div><div style="background:rgba(0,102,255,0.15);border:2px solid rgba(0,102,255,0.4);padding:0.75rem 2rem;border-radius:10px;font-weight:700;color:#4d94ff;">🎯 Orchestrator Agent</div><div style="color:rgba(0,102,255,0.4);font-size:1.2rem;">↓</div><div style="display:flex;gap:0.5rem;flex-wrap:wrap;justify-content:center;"><div style="background:rgba(77,148,255,0.1);border:1px solid rgba(77,148,255,0.3);padding:0.5rem 1rem;border-radius:8px;text-align:center;"><div style="font-size:1.2rem;">🌐</div><div style="font-size:0.75rem;font-weight:600;">Web Search</div></div><div style="background:rgba(77,148,255,0.1);border:1px solid rgba(77,148,255,0.3);padding:0.5rem 1rem;border-radius:8px;text-align:center;"><div style="font-size:1.2rem;">📈</div><div style="font-size:0.75rem;font-weight:600;">Market</div></div><div style="background:rgba(77,148,255,0.1);border:1px solid rgba(77,148,255,0.3);padding:0.5rem 1rem;border-radius:8px;text-align:center;"><div style="font-size:1.2rem;">🏆</div><div style="font-size:0.75rem;font-weight:600;">Competitor</div></div><div style="background:rgba(77,148,255,0.1);border:1px solid rgba(77,148,255,0.3);padding:0.5rem 1rem;border-radius:8px;text-align:center;"><div style="font-size:1.2rem;">⚠️</div><div style="font-size:0.75rem;font-weight:600;">SWOT</div></div><div style="background:rgba(77,148,255,0.1);border:1px solid rgba(77,148,255,0.3);padding:0.5rem 1rem;border-radius:8px;text-align:center;"><div style="font-size:1.2rem;">💡</div><div style="font-size:0.75rem;font-weight:600;">MVP</div></div><div style="background:rgba(77,148,255,0.1);border:1px solid rgba(77,148,255,0.3);padding:0.5rem 1rem;border-radius:8px;text-align:center;"><div style="font-size:1.2rem;">📄</div><div style="font-size:0.75rem;font-weight:600;">Report</div></div></div><div style="color:rgba(0,102,255,0.4);font-size:1.2rem;">↓</div><div style="background:rgba(0,212,170,0.15);border:2px solid rgba(0,212,170,0.4);padding:0.75rem 2rem;border-radius:10px;font-weight:700;color:#00d4aa;">🤖 AI Advisor → 🎯 Final Output</div></div></div>""", unsafe_allow_html=True)

# Agent Details
render_section("🎯 Agent Responsibilities")
agents = [("🎯", "Orchestrator Agent", "Coordinates all agents, manages workflow, ensures data flows correctly", "#0066ff"), ("🌐", "Web Search Agent", "Searches DuckDuckGo, Google News, Crunchbase for market intelligence", "#4d94ff"), ("📈", "Market Analysis Agent", "Analyzes market size, growth rates, trends, opportunities", "#00d4aa"), ("🏆", "Competitor Agent", "Identifies competitors, analyzes strengths/weaknesses, maps positions", "#ffd93d"), ("⚠️", "SWOT Agent", "Generates comprehensive SWOT analysis from market and competitor data", "#ff6b6b"), ("💡", "MVP Agent", "Recommends MVP features, development timeline, resources", "#4d94ff"), ("📢", "GTM Agent", "Develops go-to-market strategy including pricing and channels", "#00d4aa"), ("📄", "Report Generator", "Compiles all agent outputs into professional structured report", "#ffd93d"), ("🤖", "AI Advisor", "Provides conversational guidance and answers user questions", "#0066ff")]
for icon, name, desc, color in agents:
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;border-left:4px solid {color};"><div style="display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.5rem;">{icon}</span><div><div style="font-weight:600;font-size:0.9rem;">{name}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{desc}</div></div></div></div>', unsafe_allow_html=True)

render_section("📥 Input & Output")
col1, col2 = st.columns(2)
with col1:
    render_section("Input")
    render_table(["Agent", "Receives From", "Data"], [("Web Search", "User", "Startup parameters"), ("Market Analysis", "Web Search", "Articles, stats"), ("Competitor", "Web Search", "Competitor data"), ("SWOT", "Market + Competitor", "Analysis data"), ("MVP", "SWOT + Market", "Recommendations"), ("Report", "All agents", "Complete data")])
with col2:
    render_section("Output")
    render_table(["Agent", "Sends To", "Data"], [("Web Search", "Market + Competitor", "Structured results"), ("Market Analysis", "SWOT + MVP", "Market insights"), ("Competitor", "SWOT + Report", "Competitor analysis"), ("SWOT", "MVP + Report", "Strategic analysis"), ("MVP", "GTM + Report", "Feature plan"), ("Report", "User", "Final report")])

render_tech_badges([("🤖", "Multi-Agent Architecture"), ("🔗", "Inter-Agent Communication"), ("📊", "Data Pipelines"), ("🎯", "Orchestration"), ("🧠", "AI Models"), ("📡", "API Gateway")])

render_section("✅ Advantages")
render_advantages([("🧩", "Modular Design", "Independent agents for easy maintenance"), ("📈", "Scalability", "Add agents without disrupting existing ones"), ("🛡️", "Fault Tolerance", "Individual agent failures don't crash the system"), ("⚡", "Parallel Processing", "Multiple agents work simultaneously"), ("🎯", "Specialization", "Each agent becomes domain expert"), ("🔧", "Maintainability", "Focused codebases are easier to update")])

render_section("⚠️ Challenges")
render_challenges([("🔗", "Inter-Agent Communication", "Ensuring data consistency between agents"), ("🎯", "Orchestration Complexity", "Managing dependencies and workflows"), ("📊", "Data Duplication", "Avoiding redundant processing"), ("⏱️", "Latency", "Sequential dependencies can slow pipeline")])

render_section("🏗️ Real-World Example")
st.markdown("""<div style="background:rgba(0,102,255,0.05);border:1px solid rgba(0,102,255,0.15);border-radius:12px;padding:1.5rem;margin:1rem 0;"><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>Use Case:</strong> Validating a fintech startup idea called "PayFlow"</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>1. Web Search Agent</strong> searches for fintech market data, competitors, funding news</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>2. Market Agent</strong> analyzes the $2.1T fintech market growing at 25% CAGR</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>3. Competitor Agent</strong> identifies Stripe, Square, PayPal as top competitors</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>4. SWOT Agent</strong> identifies opportunity in SME payment processing gap</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>5. MVP Agent</strong> recommends core payment API as first feature</p><p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;"><strong>6. Report Generator</strong> compiles everything into investor-ready report</p></div>""", unsafe_allow_html=True)

render_section("🔗 Individual Agent Pages")
cols = st.columns(3)
agent_pages = [("🌐", "Web Search Agent", "02_Web_Search_Agent.py"), ("📈", "Market Analysis", "03_Market_Analysis.py"), ("🏆", "Competitor Analysis", "04_Competitor_Analysis.py"), ("⚠️", "SWOT Analysis", "05_SWOT.py"), ("💡", "MVP Recommendation", "06_MVP.py"), ("📢", "GTM Strategy", "07_GTM.py")]
for i, (icon, label, page) in enumerate(agent_pages):
    with cols[i % 3]:
        if st.button(f"{icon} {label}", use_container_width=True):
            navigate_to(page)

render_faqs([("What is multi-agent AI?", "Multi-agent AI is a system where multiple specialized AI agents work together to solve complex problems. Each agent handles a specific task."), ("How do agents communicate?", "Agents pass structured data through the Orchestrator, which manages the workflow and ensures data consistency."), ("Can I add custom agents?", "Yes! The architecture is extensible. New agents can be added by implementing the agent interface."), ("What happens if an agent fails?", "The system is fault-tolerant. If one agent fails, others can continue with available data."), ("How is data consistency maintained?", "The Orchestrator validates and transforms data between agents to ensure compatibility."), ("Can agents work in parallel?", "Yes! Independent agents can work simultaneously, while dependent agents wait for prerequisites.")])
render_summary("📋 Summary", "The Multi-Agent AI architecture uses 9 specialized agents coordinated by an Orchestrator. Each agent has a specific responsibility, from web search to report generation. This modular approach provides scalability, fault tolerance, and specialization, making the system robust and extensible.")
render_page_footer()