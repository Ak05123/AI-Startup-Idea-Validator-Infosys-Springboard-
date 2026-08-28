"""
Settings Page - Application configuration and preferences.
"""

import streamlit as st

st.set_page_config(page_title="Settings - AI Startup Idea Validator", page_icon="⚙️", layout="wide", initial_sidebar_state="collapsed")

from pathlib import Path
css_path = Path(__file__).parent.parent / "styles" / "main.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from utils.session_state import init_session_state
init_session_state()
from components.hero_section import render_page_header
from components.footer import render_footer

render_page_header("⚙️", "Settings", "Application configuration and preferences", "Home > Settings")

# ─── Application Settings ───────────────────────────────────────
st.markdown("### 🎨 Appearance")
col1, col2 = st.columns(2)
with col1:
    theme = st.selectbox(
        "Theme",
        ["Dark", "Light"],
        index=0 if st.session_state.get("settings", {}).get("theme", "dark") == "dark" else 1,
        key="settings_theme",
    )
    st.session_state["settings"]["theme"] = theme.lower()

with col2:
    animations = st.toggle(
        "Enable Animations",
        value=st.session_state.get("settings", {}).get("animations", True),
        key="settings_animations",
    )
    st.session_state["settings"]["animations"] = animations

# ─── Pipeline Settings ──────────────────────────────────────────
st.markdown("### 🔧 Pipeline Configuration")
col1, col2 = st.columns(2)
with col1:
    auto_refresh = st.toggle(
        "Auto-refresh Results",
        value=st.session_state.get("settings", {}).get("auto_refresh", False),
        key="settings_auto_refresh",
    )
    st.session_state["settings"]["auto_refresh"] = auto_refresh

with col2:
    st.markdown(
        """
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
            border-radius:12px;padding:1.25rem;height:100%;">
            <div style="font-size:0.85rem;color:rgba(255,255,255,0.5);margin-bottom:0.5rem;">
                Pipeline Status
            </div>
            <div style="display:flex;align-items:center;gap:0.5rem;">
                <div style="width:10px;height:10px;border-radius:50%;
                    background:{"#00d4aa" if st.session_state.get("pipeline_status") == "completed" else "#4d94ff" if st.session_state.get("pipeline_status") == "running" else "rgba(255,255,255,0.3)"};">
                </div>
                <span style="font-size:0.9rem;font-weight:600;">
                    {st.session_state.get("pipeline_status", "idle").title()}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─── Data Management ────────────────────────────────────────────
st.markdown("### 💾 Data Management")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔄 Reset Pipeline Data", use_container_width=True):
        from utils.session_state import reset_pipeline
        reset_pipeline()
        st.success("✅ Pipeline data has been reset.")
        st.rerun()

with col2:
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state["chat_history"] = []
        st.success("✅ Chat history cleared.")
        st.rerun()

with col3:
    if st.button("🏠 Start New Validation", use_container_width=True):
        from utils.session_state import reset_pipeline
        reset_pipeline()
        st.session_state["startup_idea"] = ""
        st.session_state["industry"] = ""
        st.session_state["country"] = ""
        st.session_state["budget"] = 0
        st.session_state["keywords"] = []
        st.session_state["form_validated"] = False
        st.success("✅ Ready for new validation!")
        st.switch_page("pages/01_Home.py")

# ─── About ──────────────────────────────────────────────────────
st.markdown("### ℹ️ About")
st.markdown(
    """
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
        border-radius:12px;padding:1.5rem;">
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;">
            <div>
                <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Application</div>
                <div style="font-size:0.9rem;font-weight:600;margin-top:0.25rem;">AI Startup Idea Validator</div>
            </div>
            <div>
                <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Version</div>
                <div style="font-size:0.9rem;font-weight:600;margin-top:0.25rem;">2.0.0</div>
            </div>
            <div>
                <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Framework</div>
                <div style="font-size:0.9rem;font-weight:600;margin-top:0.25rem;">Streamlit + Multi-Agent AI</div>
            </div>
            <div>
                <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);text-transform:uppercase;">Program</div>
                <div style="font-size:0.9rem;font-weight:600;margin-top:0.25rem;">Infosys Springboard Internship</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

render_footer()