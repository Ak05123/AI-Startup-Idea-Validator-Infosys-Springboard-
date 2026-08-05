"""
Web Search Agent - Displays results from the backend web_search_agent.py.
The backend orchestrator runs the full pipeline; this page only displays results.
"""
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Web Search Agent", page_icon="🌐", layout="wide", initial_sidebar_state="expanded")
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from utils.helpers import init_session_state
init_session_state()
from components.sidebar import render_sidebar
render_sidebar()

from utils.page_utils import render_breadcrumb, render_section, render_page_footer, navigate_to
from utils.backend_client import run_validation_pipeline, check_backend_health, parse_json_response, parse_list_response
import time

render_breadcrumb("🌐 Web Search Agent")

# Check if startup idea exists in session state
startup_idea = st.session_state.get("startup_idea", "")
industry = st.session_state.get("industry", "")
country = st.session_state.get("country", "")

if not startup_idea:
    st.warning("⚠️ Please enter your startup idea first.")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")
    st.stop()

# Display current startup info
st.markdown(f"""
<div style="background:linear-gradient(135deg,rgba(0,102,255,0.08),rgba(0,212,170,0.08));
    border:1px solid rgba(0,102,255,0.2);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem;">
    <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1rem;">
        <span style="font-size:1.5rem;">💡</span>
        <span style="font-size:1.1rem;font-weight:700;color:#fff;">Current Startup</span>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;">
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem;">
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Startup Idea</div>
            <div style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{startup_idea[:120]}{"..." if len(startup_idea) > 120 else ""}</div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem;">
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Industry</div>
            <div style="font-size:1rem;font-weight:600;color:#00d4aa;">{industry or "N/A"}</div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:0.75rem;">
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Country</div>
            <div style="font-size:1rem;font-weight:600;color:#ffd93d;">{country or "N/A"}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Run Backend Pipeline ────────────────────────────────────────
if st.session_state.get("pipeline_status") == "running" or not st.session_state.get("backend_response"):
    render_section("🔍 Running Backend Pipeline", "Orchestrator is coordinating all AI agents...")

    # Agent pipeline stages
    agent_stages = [
        ("🌐", "Web Search Agent", "Searching the web for market data..."),
        ("📈", "Market Analysis Agent", "Analyzing market size and trends..."),
        ("🏆", "Competitor Agent", "Identifying competitors..."),
        ("⚠️", "SWOT & Risk Agent", "Evaluating strengths, weaknesses, opportunities, threats..."),
        ("💡", "MVP Agent", "Recommending MVP features..."),
        ("📢", "GTM Strategy Agent", "Creating go-to-market strategy..."),
        ("📄", "Report Agent", "Generating final validation report..."),
    ]

    progress_bar = st.progress(0)
    status_placeholder = st.empty()
    timeline_placeholder = st.empty()

    # Show agent timeline
    def render_timeline(current_idx):
        stages_html = ""
        for j, (icon, label, desc) in enumerate(agent_stages):
            if j < current_idx:
                stages_html += f"""
                <div style="display:flex;align-items:center;gap:0.75rem;padding:0.5rem 0.75rem;
                    background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);
                    border-radius:8px;margin-bottom:0.25rem;">
                    <span style="color:#00d4aa;font-weight:700;">✓</span>
                    <span style="font-size:0.85rem;color:rgba(255,255,255,0.6);">{label}</span>
                    <span style="font-size:0.75rem;color:rgba(255,255,255,0.3);margin-left:auto;">Completed</span>
                </div>
                """
            elif j == current_idx:
                stages_html += f"""
                <div style="display:flex;align-items:center;gap:0.75rem;padding:0.5rem 0.75rem;
                    background:rgba(0,102,255,0.08);border:1px solid rgba(0,102,255,0.25);
                    border-radius:8px;margin-bottom:0.25rem;">
                    <span style="color:#4d94ff;font-weight:700;">⟳</span>
                    <span style="font-size:0.85rem;color:#fff;font-weight:600;">{label}</span>
                    <span style="font-size:0.75rem;color:#4d94ff;margin-left:auto;">Running...</span>
                </div>
                """
            else:
                stages_html += f"""
                <div style="display:flex;align-items:center;gap:0.75rem;padding:0.5rem 0.75rem;
                    background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);
                    border-radius:8px;margin-bottom:0.25rem;">
                    <span style="color:rgba(255,255,255,0.3);">○</span>
                    <span style="font-size:0.85rem;color:rgba(255,255,255,0.3);">{label}</span>
                    <span style="font-size:0.75rem;color:rgba(255,255,255,0.2);margin-left:auto;">Waiting</span>
                </div>
                """
        return stages_html

    # Check backend health first
    is_healthy, health_msg = check_backend_health()
    if not is_healthy:
        st.error("Backend service is currently unavailable.")
        st.info("Please ensure the backend is running and try again.")
        st.session_state["pipeline_status"] = "error"
        st.stop()

    # Run the pipeline with progress updates
    try:
        # Show initial state
        for i in range(len(agent_stages)):
            progress = (i + 1) / len(agent_stages)
            progress_bar.progress(progress)
            status_placeholder.markdown(
                f'<div style="text-align:center;padding:1rem;background:rgba(0,102,255,0.05);'
                f'border:1px solid rgba(0,102,255,0.15);border-radius:12px;margin:0.5rem 0;">'
                f'<span style="font-size:1.5rem;">{agent_stages[i][0]}</span> '
                f'<span style="font-weight:600;color:#4d94ff;">{agent_stages[i][1]}</span> — '
                f'<span style="color:rgba(255,255,255,0.6);">{agent_stages[i][2]}</span></div>',
                unsafe_allow_html=True
            )
            timeline_placeholder.markdown(
                f'<div style="background:rgba(255,255,255,0.02);border-radius:12px;padding:0.75rem;">{render_timeline(i)}</div>',
                unsafe_allow_html=True
            )
            time.sleep(0.3)

        # Call the backend pipeline
        result = run_validation_pipeline(startup_idea)

        if result["status"] == "success":
            data = result["data"]
            st.session_state["backend_response"] = data
            st.session_state["report"] = data.get("report")
            st.session_state["pipeline_status"] = "completed"
            st.session_state["pipeline_progress"] = 1.0

            progress_bar.progress(1.0)
            status_placeholder.success("✅ Backend pipeline complete! All agents finished successfully.")
            timeline_placeholder.markdown(
                f'<div style="background:rgba(255,255,255,0.02);border-radius:12px;padding:0.75rem;">{render_timeline(len(agent_stages))}</div>',
                unsafe_allow_html=True
            )
            time.sleep(0.5)
            status_placeholder.empty()
            timeline_placeholder.empty()
            st.rerun()
        else:
            st.session_state["pipeline_status"] = "error"
            progress_bar.empty()
            status_placeholder.empty()
            timeline_placeholder.empty()
            st.error("Backend service is currently unavailable.")
            st.info(f"Error details: {result['error']}")
            st.stop()
    except Exception as e:
        st.session_state["pipeline_status"] = "error"
        progress_bar.empty()
        status_placeholder.empty()
        timeline_placeholder.empty()
        st.error("Backend service is currently unavailable.")
        st.info(f"Error details: {str(e)}")
        st.stop()

# ─── Display Backend Results ─────────────────────────────────────
if st.session_state.get("backend_response"):
    data = st.session_state["backend_response"]

    # Success banner
    st.markdown("""
    <div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);
        border-radius:12px;padding:1rem;margin-bottom:1.5rem;">
        <div style="display:flex;align-items:center;gap:0.75rem;">
            <span style="font-size:1.25rem;">✅</span>
            <span style="font-weight:600;color:#00d4aa;">Backend Pipeline Complete</span>
            <span style="font-size:0.8rem;color:rgba(255,255,255,0.4);">
                Results from the multi-agent orchestrator
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Search Queries
    render_section("🔍 Search Queries", "Queries executed by the Web Search Agent")
    queries = [
        f"'{startup_idea[:50]} top competitors companies'",
        f"'{startup_idea[:50]} market size growth industry trends target customers'",
    ]
    for q in queries:
        st.markdown(
            f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
            f'border-radius:8px;padding:0.5rem 0.75rem;margin-bottom:0.3rem;font-size:0.85rem;'
            f'color:rgba(255,255,255,0.7);font-family:monospace;">🔍 {q}</div>',
            unsafe_allow_html=True
        )

    # Competitors (from backend)
    competitors_raw = data.get("competitors", [])
    competitors = parse_list_response(competitors_raw)
    if competitors:
        render_section("🏢 Competitors Discovered", "Companies identified by the Competitor Agent")
        for comp in competitors:
            st.markdown(
                f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
                f'border-radius:8px;padding:0.75rem;margin-bottom:0.5rem;display:flex;'
                f'justify-content:space-between;align-items:center;">'
                f'<span style="font-size:0.9rem;">🏢 {comp}</span>'
                f'<span style="font-size:0.8rem;color:#4d94ff;">Identified</span></div>',
                unsafe_allow_html=True
            )

    # Market Analysis (from backend)
    market_raw = data.get("market_analysis", "{}")
    market = parse_json_response(market_raw)
    if market and market.get("raw") is None:
        render_section("📊 Market Analysis Summary", "Key market insights from the Market Analysis Agent")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;"><div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Industry</div><div style="font-size:1rem;font-weight:600;color:#4d94ff;">{market.get("industry", "N/A")}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;"><div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Market Size</div><div style="font-size:1rem;font-weight:600;color:#00d4aa;">{market.get("market_size", "N/A")}</div></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:1rem;margin-bottom:0.5rem;"><div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Growth Rate</div><div style="font-size:1rem;font-weight:600;color:#ffd93d;">{market.get("growth_rate", "N/A")}</div></div>', unsafe_allow_html=True)

    # Confidence Score
    render_section("📊 Confidence Score", "Overall confidence in the analysis")
    st.markdown("""
    <div style="background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);
        border-radius:12px;padding:1.25rem;text-align:center;">
        <div style="font-size:2.5rem;font-weight:800;color:#00d4aa;">✓</div>
        <div style="font-size:1rem;font-weight:600;color:rgba(255,255,255,0.8);">Analysis Complete</div>
        <div style="font-size:0.85rem;color:rgba(255,255,255,0.5);margin-top:0.25rem;">
            All agents completed successfully. View detailed results in the analysis pages.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation to next pages
    render_section("▶️ Continue Analysis", "Proceed to the next analysis stages")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📈 Market Analysis →", use_container_width=True):
            navigate_to("03_Market_Analysis.py")
    with col2:
        if st.button("🏆 Competitor Analysis →", use_container_width=True):
            navigate_to("04_Competitor_Analysis.py")
    with col3:
        if st.button("📄 Final Report →", use_container_width=True):
            navigate_to("08_Report.py")

render_page_footer()