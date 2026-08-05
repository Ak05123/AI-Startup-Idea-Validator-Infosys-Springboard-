"""
Sidebar Navigation Component - Premium dark sidebar with glassmorphism.
"""

import streamlit as st
from streamlit_option_menu import option_menu

NAV_ITEMS = [
    {"label": "Dashboard", "icon": "🏠", "page": "Home"},
    {"label": "Startup Form", "icon": "📋", "page": "Startup_Form"},
    {"label": "Web Search", "icon": "🌐", "page": "Web_Search"},
    {"label": "Market Analysis", "icon": "📈", "page": "Market_Analysis"},
    {"label": "Competitor Analysis", "icon": "🏆", "page": "Competitor_Analysis"},
    {"label": "SWOT & Risk", "icon": "⚠️", "page": "SWOT_Risk"},
    {"label": "MVP Recommendation", "icon": "💡", "page": "MVP"},
    {"label": "Go-To-Market", "icon": "📢", "page": "GTM"},
    {"label": "Final Report", "icon": "📄", "page": "Final_Report"},
    {"label": "AI Advisor", "icon": "🤖", "page": "AI_Advisor"},
    {"label": "Settings", "icon": "⚙️", "page": "Settings"},
]


def render_sidebar() -> str:
    """
    Render the premium sidebar navigation.

    Returns:
        The selected page name as a string.
    """
    with st.sidebar:
        # Logo and branding
        st.markdown(
            """
            <div style="text-align:center;padding:1.5rem 0 0.5rem 0;">
                <div style="font-size:2.5rem;margin-bottom:0.5rem;">🚀</div>
                <div style="font-size:1.1rem;font-weight:700;
                    background:linear-gradient(135deg,#ffffff 0%,#4d94ff 50%,#00d4aa 100%);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
                    AI Validator
                </div>
                <div style="font-size:0.7rem;color:rgba(255,255,255,0.4);margin-top:0.15rem;">
                    Infosys Springboard
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Divider
        st.markdown(
            """
            <div style="height:1px;background:linear-gradient(135deg,rgba(0,102,255,0.3) 0%,rgba(0,212,170,0.3) 100%);margin:0.5rem 0 1rem 0;"></div>
            """,
            unsafe_allow_html=True,
        )

        # Navigation menu
        selected = option_menu(
            menu_title=None,
            options=[item["label"] for item in NAV_ITEMS],
            icons=[item["icon"] for item in NAV_ITEMS],
            menu_icon=None,
            default_index=0,
            styles={
                "container": {
                    "padding": "0.5rem 0",
                    "background-color": "transparent",
                },
                "nav-link": {
                    "font-size": "0.85rem",
                    "font-weight": "500",
                    "text-align": "left",
                    "margin": "0.15rem 0",
                    "padding": "0.6rem 1rem",
                    "border-radius": "10px",
                    "color": "rgba(255,255,255,0.6)",
                    "transition": "all 0.2s ease",
                },
                "nav-link-selected": {
                    "background": "linear-gradient(135deg, rgba(0,102,255,0.2) 0%, rgba(0,212,170,0.2) 100%)",
                    "border": "1px solid rgba(0,102,255,0.3)",
                    "color": "#ffffff",
                    "font-weight": "600",
                },
                "nav-link:hover": {
                    "color": "rgba(255,255,255,0.9)",
                    "background": "rgba(255,255,255,0.05)",
                },
                "icon": {
                    "font-size": "1rem",
                    "margin-right": "0.5rem",
                },
            },
        )

        # Divider
        st.markdown(
            """
            <div style="height:1px;background:linear-gradient(135deg,rgba(0,102,255,0.3) 0%,rgba(0,212,170,0.3) 100%);margin:1rem 0;"></div>
            """,
            unsafe_allow_html=True,
        )

        # Pipeline status indicator
        pipeline_status = st.session_state.get("pipeline_status", "idle")
        status_colors = {
            "idle": "rgba(255,255,255,0.3)",
            "running": "#4d94ff",
            "completed": "#00d4aa",
            "error": "#ff6b6b",
        }
        status_color = status_colors.get(pipeline_status, "rgba(255,255,255,0.3)")
        status_labels = {
            "idle": "Ready",
            "running": "Processing...",
            "completed": "Complete",
            "error": "Error",
        }

        st.markdown(
            f"""
            <div style="padding:0.75rem 1rem;background:rgba(255,255,255,0.03);border-radius:10px;margin-bottom:0.5rem;">
                <div style="display:flex;align-items:center;gap:0.5rem;">
                    <div style="width:8px;height:8px;border-radius:50%;background:{status_color};"></div>
                    <span style="font-size:0.75rem;color:rgba(255,255,255,0.5);">Pipeline: </span>
                    <span style="font-size:0.75rem;color:{status_color};font-weight:600;">{status_labels.get(pipeline_status, "Ready")}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Startup indicator
        if st.session_state.get("form_validated", False):
            st.markdown(
                """
                <div style="padding:0.75rem 1rem;background:rgba(0,212,170,0.05);border:1px solid rgba(0,212,170,0.15);border-radius:10px;margin-bottom:0.5rem;">
                    <div style="display:flex;align-items:center;gap:0.5rem;">
                        <span style="font-size:0.85rem;">✅</span>
                        <span style="font-size:0.75rem;color:#00d4aa;">Startup Validated</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Bottom info
        st.markdown(
            """
            <div style="margin-top:2rem;padding:1rem;text-align:center;">
                <div style="font-size:0.7rem;color:rgba(255,255,255,0.3);">
                    v2.0.0 — Infosys Springboard
                </div>
                <div style="margin-top:0.5rem;">
                    <a href="https://github.com/Ak05123/AI-Startup-Idea-Validator-Infosys-Springboard-"
                       target="_blank" style="color:rgba(255,255,255,0.4);text-decoration:none;font-size:0.75rem;">
                        📦 GitHub
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Map label to page name
    label_to_page = {item["label"]: item["page"] for item in NAV_ITEMS}
    return label_to_page.get(selected, "Home")