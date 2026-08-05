"""
Sidebar component for the AI Startup Idea Validator.
"""

import streamlit as st
from streamlit_option_menu import option_menu

from utils.theme import SIDEBAR_ITEMS


def render_sidebar() -> str:
    """
    Render the sidebar navigation with a modern design.

    Returns:
        The selected page name as a string.
    """
    with st.sidebar:
        # Logo and branding
        st.markdown(
            """
            <div style="text-align: center; padding: 1.5rem 0 0.5rem 0;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🚀</div>
                <div style="font-size: 1.1rem; font-weight: 700; background: linear-gradient(135deg, #ffffff 0%, #4d94ff 50%, #00d4aa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                    AI Validator
                </div>
                <div style="font-size: 0.7rem; color: rgba(255,255,255,0.4); margin-top: 0.15rem;">
                    Infosys Springboard
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Navigation menu
        selected = option_menu(
            menu_title=None,
            options=[item["label"] for item in SIDEBAR_ITEMS],
            icons=[item["icon"] for item in SIDEBAR_ITEMS],
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
            <div style="height: 1px; background: linear-gradient(135deg, rgba(0,102,255,0.3) 0%, rgba(0,212,170,0.3) 100%); margin: 1rem 0;"></div>
            """,
            unsafe_allow_html=True,
        )

        # Settings section
        st.markdown(
            """
            <div style="font-size: 0.7rem; color: rgba(255,255,255,0.3); text-transform: uppercase; letter-spacing: 1px; padding: 0.5rem 1rem;">
                Settings
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("⚙️ Settings", use_container_width=True, key="settings_btn"):
            st.session_state.current_page = "Settings"

        # Bottom info
        st.markdown(
            """
            <div style="margin-top: 2rem; padding: 1rem; text-align: center;">
                <div style="font-size: 0.7rem; color: rgba(255,255,255,0.3);">
                    v1.0.0 — Infosys Springboard
                </div>
                <div style="margin-top: 0.5rem;">
                    <a href="https://github.com/Ak05123/AI-Startup-Idea-Validator-Infosys-Springboard-" target="_blank" style="color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.75rem; transition: color 0.2s;" onmouseover="this.style.color='#4d94ff'" onmouseout="this.style.color='rgba(255,255,255,0.4)'">
                        📦 GitHub
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Map label back to page name
    label_to_page = {item["label"]: item["page"] for item in SIDEBAR_ITEMS}
    return label_to_page.get(selected, "Home")