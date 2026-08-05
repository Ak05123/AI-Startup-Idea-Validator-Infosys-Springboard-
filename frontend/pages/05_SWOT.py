"""SWOT Analysis - Strategic analysis of strengths, weaknesses, opportunities, threats."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="SWOT Analysis", page_icon="⚠️", layout="wide", initial_sidebar_state="expanded")
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

render_breadcrumb("⚠️ SWOT Analysis")
render_hero("⚠️", "SWOT Analysis", "Strategic analysis of strengths, weaknesses, opportunities, and threats", "SWOT Analysis is a strategic planning tool that evaluates a business's Strengths, Weaknesses, Opportunities, and Threats. Our AI generates comprehensive SWOT analysis based on market research, competitor data, and industry trends.")

data = get_market_data()
swot = data.get("swot", {})

render_section("🔍 What is SWOT Analysis?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>SWOT Analysis</strong> is a framework for evaluating a company's competitive position. It assesses internal factors (Strengths and Weaknesses) and external factors (Opportunities and Threats). AI-powered SWOT analysis automates data collection and provides objective, data-driven strategic insights.</p></div>""", unsafe_allow_html=True)

render_section("🎯 Why is it Important?")
st.markdown("""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><p><strong>Strategic Clarity:</strong> Understand your competitive position clearly.</p><p><strong>Risk Awareness:</strong> Identify threats before they become problems.</p><p><strong>Opportunity Recognition:</strong> Spot market opportunities early.</p><p><strong>Resource Allocation:</strong> Focus resources where they matter most.</p><p><strong>Investor Communication:</strong> Demonstrate strategic thinking to investors.</p></div>""", unsafe_allow_html=True)

render_section("⚙️ How AI Generates SWOT")
cols = st.columns(4)
for i, (num, title, desc) in enumerate([("1", "Data Collection", "Gather internal/external data"), ("2", "Pattern Analysis", "Identify strategic patterns"), ("3", "Classification", "Categorize into SWOT"), ("4", "Recommendations", "Generate strategic actions")]):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1rem;background:rgba(0,102,255,0.05);border:1px solid rgba(0,102,255,0.15);border-radius:10px;"><div style="font-size:1.5rem;font-weight:700;color:#4d94ff;">{num}</div><div style="font-weight:600;font-size:0.85rem;">{title}</div><div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{desc}</div></div>', unsafe_allow_html=True)

def render_swot_quadrant(title, items, icon, color):
    items_html = "".join(f'<div style="padding:0.5rem 0;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;align-items:flex-start;gap:0.5rem;"><span style="color:{color};font-size:1rem;">▸</span><span style="font-size:0.85rem;color:rgba(255,255,255,0.7);">{item}</span></div>' for item in items)
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid {color}33;border-radius:12px;padding:1.25rem;height:100%;"><div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.75rem;"><span style="font-size:1.5rem;">{icon}</span><span style="font-size:1rem;font-weight:700;color:{color};">{title}</span></div>{items_html}</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    render_swot_quadrant("Strengths", swot.get("strengths",[]), "💪", "#00d4aa")
with col2:
    render_swot_quadrant("Weaknesses", swot.get("weaknesses",[]), "⚠️", "#ff6b6b")
col1, col2 = st.columns(2)
with col1:
    render_swot_quadrant("Opportunities", swot.get("opportunities",[]), "🚀", "#4d94ff")
with col2:
    render_swot_quadrant("Threats", swot.get("threats",[]), "🔥", "#ffd93d")

render_section("📥 Input & Output")
col1, col2 = st.columns(2)
with col1:
    render_section("Input")
    render_table(["Source", "Data"], [("Market Analysis", "Market size, growth, trends"), ("Competitor Analysis", "Competitor strengths/weaknesses"), ("Web Search", "News, discussions, reviews"), ("Industry Reports", "Market research data")])
with col2:
    render_section("Output")
    render_table(["Output", "Description"], [("Strengths", "Internal advantages"), ("Weaknesses", "Internal limitations"), ("Opportunities", "External possibilities"), ("Threats", "External risks"), ("Strategy", "Recommended actions")])

render_tech_badges([("🤖", "NLP Analysis"), ("📊", "Pattern Recognition"), ("🧠", "AI Classification"), ("📈", "Strategic Modeling")])

render_section("🎯 Strategic Recommendations")
recommendations = [("SO Strategy", "Leverage multi-agent AI to capture growing SME demand", "#00d4aa"), ("WO Strategy", "Partner with accelerators to overcome team size limitations", "#4d94ff"), ("ST Strategy", "Use AI-native advantages against legacy competitors", "#ffd93d"), ("WT Strategy", "Build modular architecture to reduce API dependency", "#ff6b6b")]
for strategy, desc, color in recommendations:
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;border-left:4px solid {color};"><div style="font-weight:600;font-size:0.9rem;color:{color};">{strategy}</div><div style="font-size:0.85rem;color:rgba(255,255,255,0.6);margin-top:0.25rem;">{desc}</div></div>', unsafe_allow_html=True)

render_faqs([("What is SWOT Analysis?", "SWOT stands for Strengths, Weaknesses, Opportunities, and Threats. It's a strategic framework for evaluating a company's competitive position."), ("How does AI generate SWOT?", "AI analyzes market data, competitor information, and industry trends to objectively identify SWOT factors."), ("How often should SWOT be updated?", "SWOT should be reviewed quarterly or when significant market changes occur."), ("Can SWOT predict future challenges?", "SWOT helps identify potential threats and opportunities, enabling proactive strategic planning."), ("What makes a good SWOT analysis?", "A good SWOT is specific, data-driven, and leads to actionable strategic recommendations."), ("How does SWOT differ from competitor analysis?", "SWOT focuses on your own business position, while competitor analysis focuses on competitors.")])
render_summary("📋 Summary", "The SWOT analysis reveals a strong internal position with multi-agent AI architecture as the key differentiator. External opportunities in the SME segment and international markets present significant growth potential. Primary threats include established competitors and rapid technological change. Recommended strategy: leverage AI advantages to capture underserved SME market.")
render_page_footer()