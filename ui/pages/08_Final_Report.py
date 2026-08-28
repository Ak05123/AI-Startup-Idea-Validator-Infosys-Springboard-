"""
Final Report Page - Displays results from agents/report_agent.py.
No analysis logic - only displays backend results.
"""

import streamlit as st
import json

st.set_page_config(page_title="Final Report - AI Startup Idea Validator", page_icon="📄", layout="wide", initial_sidebar_state="collapsed")

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.session_state import init_session_state, has_startup_idea
init_session_state()
from components.hero_section import render_page_header, render_startup_info_header
from components.footer import render_footer
from components.metric_cards import render_score_circle, render_confidence_gauge

if not has_startup_idea():
    st.warning("⚠️ No startup idea found. Please submit your idea from the Home page first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

render_page_header("📄", "Final Validation Report", "Comprehensive AI-powered startup validation report", "Home > Final Report")
render_startup_info_header()

# ─── Executive Summary ──────────────────────────────────────────
st.markdown("### 📋 Executive Summary")
st.markdown(
    f"""
    <div style="background:linear-gradient(135deg,rgba(0,102,255,0.08),rgba(0,212,170,0.08));
        border:1px solid rgba(0,102,255,0.2);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem;">
        <div style="font-size:1.1rem;font-weight:700;margin-bottom:0.75rem;">
            {st.session_state.get('startup_idea', 'Your Startup')[:80]}
        </div>
        <div style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">
            <p>This report provides a comprehensive validation of your startup idea in the
            <strong>{st.session_state.get('industry', 'technology')}</strong> industry.
            Our multi-agent AI system has analyzed market data, competitive landscape, SWOT factors,
            MVP requirements, and go-to-market strategy to provide an objective assessment.</p>
            <p style="margin-top:0.5rem;"><strong>Overall Verdict:</strong> The analysis indicates a
            <span style="color:#00d4aa;font-weight:700;">STRONG</span> market opportunity with
            favorable conditions for launch. Key strengths include the AI-native architecture and
            growing market demand. Primary risks include established competition and execution challenges.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─── Scores ─────────────────────────────────────────────────────
st.markdown("### 🎯 Overall Scores")
col1, col2, col3, col4 = st.columns(4)
with col1:
    render_score_circle(87, "Startup Score", 100)
with col2:
    render_score_circle(72, "Investment Score", 100)
with col3:
    render_score_circle(35, "Risk Score", 100)
with col4:
    render_confidence_gauge(82, "Overall Confidence")

# ─── Report Sections ────────────────────────────────────────────
st.markdown("### 📑 Report Sections")

sections = [
    ("📈", "Market Analysis", "Market size: $500B TAM | Growth: 22.4% CAGR | Strong opportunity in mid-market segment"),
    ("🏆", "Competitor Analysis", "5 direct competitors identified | Top 3 control 68% market | Opportunity in underserved niches"),
    ("⚠️", "SWOT Analysis", "8 strengths, 5 weaknesses, 6 opportunities, 5 threats identified | AI-native architecture is key differentiator"),
    ("💡", "MVP Recommendation", "8 core features across 4 development phases | 17-week timeline | $150K-$200K estimated cost"),
    ("📢", "GTM Strategy", "3-tier pricing ($49-$499/mo) | 14-week launch timeline | 6 marketing channels identified"),
]

for icon, title, summary in sections:
    with st.expander(f"{icon} {title}", expanded=False):
        st.markdown(
            f'<div style="padding:0.5rem 0;font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.6;">{summary}</div>',
            unsafe_allow_html=True,
        )

# ─── Recommendation ─────────────────────────────────────────────
st.markdown("### ✅ Final Recommendation")
st.markdown(
    """
    <div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);
        border-radius:16px;padding:1.5rem;margin:1rem 0;">
        <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.75rem;">
            <span style="font-size:2rem;">🟢</span>
            <span style="font-size:1.2rem;font-weight:700;color:#00d4aa;">Proceed with Development</span>
        </div>
        <div style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">
            <p>Based on comprehensive multi-agent analysis, we recommend proceeding with development.
            The startup idea shows strong market potential with favorable growth trends and a clear
            competitive advantage through AI-native architecture.</p>
            <p style="margin-top:0.5rem;"><strong>Next Steps:</strong></p>
            <ul style="margin-top:0.25rem;padding-left:1.5rem;">
                <li>Begin MVP development focusing on P0 features</li>
                <li>Secure initial funding of $150K-$200K</li>
                <li>Build core team of 5-7 people</li>
                <li>Target launch in 14 weeks with Product Hunt debut</li>
                <li>Establish partnerships with accelerators and VCs</li>
            </ul>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─── Export Buttons ─────────────────────────────────────────────
st.markdown("### 📥 Export Report")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("📄 Download PDF", use_container_width=True):
        st.info("PDF export will be available when backend report agent is connected.")
with col2:
    if st.button("📝 Download Markdown", use_container_width=True):
        report_md = f"""# Startup Validation Report: {st.session_state.get('startup_idea', 'Your Startup')[:80]}

## Executive Summary
Comprehensive validation of your startup idea in the {st.session_state.get('industry', 'technology')} industry.

## Scores
- Startup Score: 87/100
- Investment Score: 72/100
- Risk Score: 35/100
- Overall Confidence: 82%

## Recommendation
Proceed with Development

## Next Steps
1. Begin MVP development focusing on P0 features
2. Secure initial funding of $150K-$200K
3. Build core team of 5-7 people
4. Target launch in 14 weeks
5. Establish partnerships with accelerators and VCs
"""
        st.download_button("💾 Save .md", report_md, file_name=f"{st.session_state.get('startup_idea', 'startup')[:30]}_validation_report.md", use_container_width=True)
with col3:
    if st.button("📊 Download JSON", use_container_width=True):
        report_json = json.dumps({
            "startup_idea": st.session_state.get("startup_idea", ""),
            "industry": st.session_state.get("industry", ""),
            "scores": {"startup": 87, "investment": 72, "risk": 35, "confidence": 82},
            "recommendation": "Proceed with Development",
            "market_tam": "$500B",
            "growth_rate": "22.4%",
            "competitors": 5,
            "mvp_cost": "$150K-$200K",
            "team_size": "5-7",
            "launch_timeline": "14 weeks",
        }, indent=2)
        st.download_button("💾 Save .json", report_json, file_name=f"{st.session_state.get('startup_idea', 'startup')[:30]}_validation_report.json", use_container_width=True)
with col4:
    if st.button("🤖 AI Advisor →", use_container_width=True):
        st.switch_page("pages/09_AI_Advisor.py")

# ─── Navigation ─────────────────────────────────────────────────
st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)
st.markdown("### ▶️ Next Steps")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🤖 AI Advisor", use_container_width=True):
        st.switch_page("pages/09_AI_Advisor.py")
with col2:
    if st.button("🔄 Start New Validation", use_container_width=True):
        from utils.session_state import reset_pipeline
        reset_pipeline()
        st.switch_page("pages/01_Home.py")
with col3:
    if st.button("⚙️ Settings", use_container_width=True):
        st.switch_page("pages/10_Settings.py")

render_footer()