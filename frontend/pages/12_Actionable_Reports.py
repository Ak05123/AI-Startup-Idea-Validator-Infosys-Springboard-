"""Actionable Reports - Transform data into practical business recommendations."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Actionable Reports", page_icon="📋", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()
from utils.page_utils import render_breadcrumb, render_hero, render_section, render_card, render_workflow, render_tech_badges, render_table, render_advantages, render_challenges, render_faqs, render_summary, render_page_footer
from utils.helpers import get_market_data

render_breadcrumb("📋 Actionable Reports")
render_hero("📋", "Actionable Reports", "Transform collected data into practical business recommendations", "Actionable reports bridge the gap between raw data and business decisions. Our AI analyzes market intelligence, competitor data, and industry trends to generate clear, prioritized recommendations you can act on immediately.")

data = get_market_data()

render_section("🔍 What are Actionable Reports?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Actionable Reports</strong> transform raw data and analysis into specific, prioritized recommendations. Unlike traditional reports that just present information, actionable reports tell you exactly what to do, why to do it, and what priority it should be. They bridge the gap between analysis and execution.</p></div>""", unsafe_allow_html=True)

render_section("🎯 Why is it Important?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Save Time:</strong> Hours of research condensed into actionable insights.</p><p><strong>Prioritized Actions:</strong> Clear ranking of what to do first.</p><p><strong>Better Decisions:</strong> Data-backed recommendations reduce guesswork.</p><p><strong>Team Alignment:</strong> Everyone knows what needs to be done.</p><p><strong>Measurable Outcomes:</strong> Clear KPIs and success metrics.</p></div>""", unsafe_allow_html=True)

render_section("⚡ How It Works")
render_workflow([("📊", "Data Collection", "Gather from multiple sources"), ("🤖", "AI Analysis", "Process and identify patterns"), ("📋", "Report Generation", "Create structured reports"), ("🎯", "Action Items", "Prioritized recommendations")])

render_section("🔑 Key Findings")
findings = [("📊", "Market Opportunity", "The AI validation market is projected to reach $8.5B by 2028, growing at 22.4% CAGR"), ("🏆", "Competitive Landscape", "5 major competitors identified; opportunity in SME segment with AI-native features"), ("⚠️", "Risk Assessment", "Primary risks: competition from established players and data accuracy challenges"), ("💡", "Technology Advantage", "Multi-agent AI architecture provides significant differentiation from legacy solutions")]
for icon, title, desc in findings:
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;"><div style="display:flex;align-items:center;gap:0.75rem;"><span style="font-size:1.5rem;">{icon}</span><div><div style="font-weight:600;font-size:0.9rem;">{title}</div><div style="font-size:0.85rem;color:rgba(255,255,255,0.5);">{desc}</div></div></div></div>', unsafe_allow_html=True)

render_section("💡 Recommendations")
recommendations = [("P0", "Develop Core AI Search Agent", "Build multi-source search pipeline with DuckDuckGo", "#ff6b6b"), ("P0", "Create Market Analysis Dashboard", "Visualize market data with Plotly charts", "#ff6b6b"), ("P1", "Implement Competitor Tracking", "Automated competitor monitoring", "#ffd93d"), ("P1", "Build Export & Reporting", "PDF, CSV, JSON downloads", "#ffd93d"), ("P2", "Launch AI Advisor Chat", "Interactive AI advisory interface", "#4d94ff")]
for priority, title, desc, color in recommendations:
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem 1rem;margin-bottom:0.5rem;border-left:4px solid {color};"><div style="display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.9rem;">{title}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{desc}</div></div><span style="background:{color}22;color:{color};padding:2px 10px;border-radius:10px;font-size:0.75rem;font-weight:600;">{priority}</span></div></div>', unsafe_allow_html=True)

render_section("⚠️ Business Risks & 🚀 Opportunities")
col1, col2 = st.columns(2)
with col1:
    risks = data.get("market_risks",[])
    for risk in risks:
        st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:0.75rem;margin-bottom:0.5rem;"><div style="font-size:0.85rem;font-weight:500;">{risk.get("risk","")}</div><div style="font-size:0.75rem;color:#ffd93d;">⚠️ {risk.get("probability",0)*100:.0f}% probability</div><div style="font-size:0.75rem;color:#00d4aa;">✅ {risk.get("mitigation","")}</div></div>', unsafe_allow_html=True)
with col2:
    opportunities = [("SME Market Segment", "$2.1B untapped market"), ("AI-Powered Features", "Multi-agent as competitive moat"), ("International Expansion", "APAC 35% growth"), ("Partnership Ecosystem", "Accelerators as channels")]
    for title, desc in opportunities:
        st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:0.75rem;margin-bottom:0.5rem;"><div style="font-weight:600;font-size:0.85rem;">{title}</div><div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{desc}</div></div>', unsafe_allow_html=True)

render_section("🕳️ Market Gaps")
cols = st.columns(4)
gaps = [("Affordable AI Validation", "No SME-friendly pricing"), ("Real-time Multi-Source", "Single source limitations"), ("Automated Reports", "Manual creation is slow"), ("Integrated AI Advisor", "No conversational AI")]
for i, (title, desc) in enumerate(gaps):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;height:100%;"><div style="font-weight:600;font-size:0.8rem;margin-bottom:0.25rem;">{title}</div><div style="font-size:0.7rem;color:rgba(255,255,255,0.5);">{desc}</div></div>', unsafe_allow_html=True)

render_section("📊 Priority Matrix")
st.markdown("""<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;"><div style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;"><div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);border-radius:10px;padding:1rem;"><div style="font-weight:600;color:#00d4aa;font-size:0.85rem;">🏆 Quick Wins (High Impact, Low Effort)</div><ul style="list-style:none;padding:0;font-size:0.8rem;margin-top:0.5rem;"><li>▸ AI Search Agent</li><li>▸ Market Dashboard</li><li>▸ Export Features</li></ul></div><div style="background:rgba(77,148,255,0.05);border:1px solid rgba(77,148,255,0.15);border-radius:10px;padding:1rem;"><div style="font-weight:600;color:#4d94ff;font-size:0.85rem;">💎 Major Projects (High Impact, High Effort)</div><ul style="list-style:none;padding:0;font-size:0.8rem;margin-top:0.5rem;"><li>▸ AI Advisor Chat</li><li>▸ Full Automation Pipeline</li></ul></div><div style="background:rgba(255,217,61,0.05);border:1px solid rgba(255,217,61,0.15);border-radius:10px;padding:1rem;"><div style="font-weight:600;color:#ffd93d;font-size:0.85rem;">🔧 Fill-Ins (Low Impact, Low Effort)</div><ul style="list-style:none;padding:0;font-size:0.8rem;margin-top:0.5rem;"><li>▸ Dashboard Polish</li><li>▸ Documentation</li></ul></div><div style="background:rgba(255,107,107,0.05);border:1px solid rgba(255,107,107,0.15);border-radius:10px;padding:1rem;"><div style="font-weight:600;color:#ff6b6b;font-size:0.85rem;">🕳️ Avoid (Low Impact, High Effort)</div><ul style="list-style:none;padding:0;font-size:0.8rem;margin-top:0.5rem;"><li>▸ Custom CSS Themes</li><li>▸ Legacy API Support</li></ul></div></div></div>""", unsafe_allow_html=True)

render_section("📋 Next Steps")
cols = st.columns(4)
steps = [("Week 1-2", "Setup infrastructure", "#0066ff"), ("Week 3-4", "Build Web Search Agent", "#4d94ff"), ("Week 5-6", "Market Analysis + Competitor", "#00d4aa"), ("Week 7-8", "Reporting + AI Advisor", "#ffd93d")]
for i, (timeline, desc, color) in enumerate(steps):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;border-top:4px solid {color};height:100%;"><div style="font-size:0.85rem;font-weight:700;color:{color};">{timeline}</div><div style="font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:0.25rem;">{desc}</div></div>', unsafe_allow_html=True)

render_faqs([("What makes a report 'actionable'?", "An actionable report provides specific, prioritized recommendations rather than just data. It tells you exactly what to do and why."), ("How are recommendations prioritized?", "Recommendations are ranked by impact vs. effort analysis, with quick wins prioritized first."), ("Can I customize the reports?", "Yes! The reporting system is modular and can be customized for different stakeholder needs."), ("How often should I generate reports?", "We recommend generating reports after each major search or at least weekly during active validation."), ("What formats are supported?", "Reports can be exported as JSON, Markdown, and CSV. PDF export is coming soon."), ("How are KPIs measured?", "Each recommendation includes success metrics and KPIs to track implementation progress.")])
render_summary("📋 Summary", "Actionable Reports transform market intelligence into prioritized, executable recommendations. By focusing on impact vs. effort, they ensure you always know what to do next. Start with quick wins (AI Search Agent, Market Dashboard) and progress to major projects (AI Advisor, Full Automation).")
render_page_footer()