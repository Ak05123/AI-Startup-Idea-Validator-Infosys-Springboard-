"""Final Report - Dynamic validation report using the submitted startup idea and analysis data."""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Final Report", page_icon="📄", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()
from utils.page_utils import render_breadcrumb, render_section, render_table, render_faqs, render_summary, render_page_footer, navigate_to
from utils.helpers import get_search_results, get_competitor_data, get_market_data
import json

startup_name = st.session_state.get("startup_name", "")
startup_idea = st.session_state.get("startup_idea", "")
industry = st.session_state.get("industry", "")
country = st.session_state.get("country", "")
stage = st.session_state.get("stage", "")
budget = st.session_state.get("budget", 0)
keywords = st.session_state.get("keywords", [])

if not startup_idea:
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_breadcrumb("📄 Final Report")

# Load data from session state or fallback to mock data
search_data = st.session_state.get("search_results") or get_search_results()
competitor_data = st.session_state.get("competitor_data") or get_competitor_data()
market_data = st.session_state.get("market_data") or get_market_data()

stats = search_data.get("market_statistics", {})
swot = market_data.get("swot", {})
overview = market_data.get("market_overview", {})
competitors = competitor_data.get("direct_competitors", [])

# Report Header
st.markdown(f"""
<div style="text-align:center;padding:2.5rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;margin-bottom:1.5rem;">
    <div style="font-size:3rem;margin-bottom:0.75rem;">📄</div>
    <div style="font-size:1.5rem;font-weight:800;background:linear-gradient(135deg,#fff,#4d94ff,#00d4aa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">AI Startup Idea Validator</div>
    <div style="font-size:1.1rem;font-weight:600;color:#4d94ff;margin-top:0.5rem;">{startup_name or "Startup Idea"}</div>
    <div style="font-size:0.9rem;color:rgba(255,255,255,0.5);margin-top:0.25rem;">{industry or "N/A"} | {country or "N/A"} | {stage or "N/A"}</div>
</div>
""", unsafe_allow_html=True)

# Executive Summary
render_section("📋 Executive Summary")
st.markdown(f"""
<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;">
<p>This report presents a comprehensive validation analysis for <strong>{startup_name or 'your startup idea'}</strong> in the <strong>{industry or 'target'}</strong> industry.</p>
<p>Based on research across {len(stats.get('sources_used',[]))} sources.</p>
<p><strong>Startup Idea:</strong> {startup_idea}</p>
<p>The market is projected to reach <strong>{overview.get('total_addressable_market','$8.5B')} by 2028</strong>, growing at a <strong>{overview.get('market_growth_rate','22.4%')} CAGR</strong>.</p>
</div>
""", unsafe_allow_html=True)

# Scores
render_section("📊 Validation Scores")
cols = st.columns(4)
scores = [("Market Score", "85/100", "High potential", "#4d94ff"), ("Competition Score", "72/100", "Moderate competition", "#00d4aa"), ("Investment Score", "88/100", "Investor ready", "#ffd93d"), ("Risk Score", "65/100", "Manageable risks", "#ff6b6b")]
for i, (label, score, desc, color) in enumerate(scores):
    with cols[i]:
        st.markdown(f'<div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid {color}33;border-radius:12px;"><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{label}</div><div style="font-size:2rem;font-weight:700;color:{color};margin:0.25rem 0;">{score}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{desc}</div></div>', unsafe_allow_html=True)

# Market Analysis Summary
render_section("📈 Market Analysis Summary")
st.markdown(f"""<div style="font-size:0.95rem;color:rgba(255,255,255,0.7);line-height:1.8;"><table style="width:100%;border-collapse:collapse;">
<tr><td style="padding:0.5rem;border-bottom:1px solid rgba(255,255,255,0.05);"><strong>TAM</strong></td><td style="padding:0.5rem;border-bottom:1px solid rgba(255,255,255,0.05);">{overview.get('total_addressable_market','N/A')}</td></tr>
<tr><td style="padding:0.5rem;border-bottom:1px solid rgba(255,255,255,0.05);"><strong>SAM</strong></td><td style="padding:0.5rem;border-bottom:1px solid rgba(255,255,255,0.05);">{overview.get('serviceable_addressable_market','N/A')}</td></tr>
<tr><td style="padding:0.5rem;border-bottom:1px solid rgba(255,255,255,0.05);"><strong>Growth Rate</strong></td><td style="padding:0.5rem;border-bottom:1px solid rgba(255,255,255,0.05);">{overview.get('market_growth_rate','N/A')}</td></tr>
<tr><td style="padding:0.5rem;"><strong>CAGR</strong></td><td style="padding:0.5rem;">{overview.get('cagr_5year','N/A')}</td></tr>
</table></div>""", unsafe_allow_html=True)

# Competitor Summary
render_section("🏆 Competitor Summary")
for comp in competitors[:3]:
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:0.75rem;margin-bottom:0.5rem;"><div style="display:flex;justify-content:space-between;"><div><div style="font-weight:600;font-size:0.9rem;">{comp.get("name","")}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{comp.get("description","")}</div></div><div style="text-align:right;"><div style="font-size:0.85rem;font-weight:600;color:#4d94ff;">{comp.get("market_share",0)}% share</div><div style="font-size:0.75rem;color:rgba(255,255,255,0.4);">💰 {comp.get("funding","N/A")}</div></div></div></div>', unsafe_allow_html=True)

# SWOT
render_section("⚠️ SWOT Analysis")
col1, col2 = st.columns(2)
with col1:
    strengths = "".join(f'<li style="padding:0.25rem 0;font-size:0.85rem;color:rgba(255,255,255,0.7);">▸ {s}</li>' for s in swot.get("strengths",[]))
    st.markdown(f'<div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);border-radius:10px;padding:1rem;margin-bottom:0.5rem;"><div style="font-weight:600;color:#00d4aa;margin-bottom:0.5rem;">💪 Strengths</div><ul style="list-style:none;padding:0;">{strengths}</ul></div>', unsafe_allow_html=True)
    opportunities = "".join(f'<li style="padding:0.25rem 0;font-size:0.85rem;color:rgba(255,255,255,0.7);">▸ {o}</li>' for o in swot.get("opportunities",[]))
    st.markdown(f'<div style="background:rgba(77,148,255,0.05);border:1px solid rgba(77,148,255,0.15);border-radius:10px;padding:1rem;"><div style="font-weight:600;color:#4d94ff;margin-bottom:0.5rem;">🚀 Opportunities</div><ul style="list-style:none;padding:0;">{opportunities}</ul></div>', unsafe_allow_html=True)
with col2:
    weaknesses = "".join(f'<li style="padding:0.25rem 0;font-size:0.85rem;color:rgba(255,255,255,0.7);">▸ {w}</li>' for w in swot.get("weaknesses",[]))
    st.markdown(f'<div style="background:rgba(255,107,107,0.05);border:1px solid rgba(255,107,107,0.15);border-radius:10px;padding:1rem;margin-bottom:0.5rem;"><div style="font-weight:600;color:#ff6b6b;margin-bottom:0.5rem;">⚠️ Weaknesses</div><ul style="list-style:none;padding:0;">{weaknesses}</ul></div>', unsafe_allow_html=True)
    threats = "".join(f'<li style="padding:0.25rem 0;font-size:0.85rem;color:rgba(255,255,255,0.7);">▸ {t}</li>' for t in swot.get("threats",[]))
    st.markdown(f'<div style="background:rgba(255,217,61,0.05);border:1px solid rgba(255,217,61,0.15);border-radius:10px;padding:1rem;"><div style="font-weight:600;color:#ffd93d;margin-bottom:0.5rem;">🔥 Threats</div><ul style="list-style:none;padding:0;">{threats}</ul></div>', unsafe_allow_html=True)

# Recommendations
render_section("💡 Recommendations")
recommendations = [
    ("P0", "Develop AI Search Agent", "Multi-source search with DuckDuckGo integration"),
    ("P0", "Market Analysis Dashboard", "Interactive charts and market intelligence"),
    ("P1", "Competitor Tracking", "Automated competitor monitoring"),
    ("P1", "Export & Reporting", "CSV, JSON, PDF downloads"),
    ("P2", "AI Advisor Chat", "Conversational AI advisory interface"),
]
for priority, title, desc in recommendations:
    color = "#ff6b6b" if priority == "P0" else "#ffd93d" if priority == "P1" else "#4d94ff"
    st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:0.75rem;margin-bottom:0.5rem;border-left:4px solid {color};"><div style="display:flex;justify-content:space-between;align-items:center;"><div><div style="font-weight:600;font-size:0.9rem;">{title}</div><div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{desc}</div></div><span style="background:{color}22;color:{color};padding:2px 10px;border-radius:10px;font-size:0.75rem;font-weight:600;">{priority}</span></div></div>', unsafe_allow_html=True)

# Sources
render_section("📚 Sources")
sources = stats.get("sources_used", [])
cols = st.columns(4)
for i, source in enumerate(sources):
    with cols[i % 4]:
        st.markdown(f'<div style="text-align:center;padding:0.75rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;"><div style="font-size:0.85rem;font-weight:500;">{source}</div></div>', unsafe_allow_html=True)

# Export
render_section("📤 Export Report")
report_data = {
    "startup_name": startup_name,
    "startup_idea": startup_idea,
    "industry": industry,
    "country": country,
    "stage": stage,
    "budget": budget,
    "keywords": keywords,
    "market_analysis": overview,
    "competitors": [c["name"] for c in competitors],
    "swot": swot,
    "recommendations": [r[1] for r in recommendations],
    "sources": sources,
}
col1, col2, col3 = st.columns(3)
with col1:
    st.download_button("📥 Download JSON", data=json.dumps(report_data, indent=2), file_name=f"{startup_name or 'startup'}_validation_report.json", mime="application/json", use_container_width=True)
with col2:
    md_content = f"""# Validation Report: {startup_name or 'Startup Idea'}

## Executive Summary
{startup_idea}

## Market Analysis
- **TAM:** {overview.get('total_addressable_market', 'N/A')}
- **SAM:** {overview.get('serviceable_addressable_market', 'N/A')}
- **Growth Rate:** {overview.get('market_growth_rate', 'N/A')}
- **CAGR:** {overview.get('cagr_5year', 'N/A')}

## Competitors
{chr(10).join(f'- {c["name"]} ({c.get("market_share", 0)}% share)' for c in competitors[:5])}

## SWOT
- **Strengths:** {', '.join(swot.get('strengths', []))}
- **Weaknesses:** {', '.join(swot.get('weaknesses', []))}
- **Opportunities:** {', '.join(swot.get('opportunities', []))}
- **Threats:** {', '.join(swot.get('threats', []))}
"""
    st.download_button("📥 Download Markdown", data=md_content, file_name=f"{startup_name or 'startup'}_report.md", mime="text/markdown", use_container_width=True)
with col3:
    if st.button("🔄 Regenerate Report", use_container_width=True):
        st.rerun()

render_summary("📋 Final Verdict",
    f"Based on comprehensive analysis of <strong>{startup_name or 'your startup idea'}</strong> in the <strong>{industry or 'target'}</strong> industry, "
    f"this startup idea shows strong potential with a market growing at {overview.get('market_growth_rate', '22.4%')}.")

render_page_footer()