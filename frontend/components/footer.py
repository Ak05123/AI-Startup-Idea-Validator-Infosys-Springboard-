"""
Footer component for the AI Startup Idea Validator.
"""

import streamlit as st
from datetime import datetime


def render_footer() -> None:
    """Render a premium footer with links and branding."""
    current_year = datetime.now().year
    
    st.markdown(
        f"""
        <div class="footer">
            <div class="footer-text">
                © {current_year} AI Startup Idea Validator — Infosys Springboard Virtual Internship
            </div>
            <div class="footer-links">
                <a href="https://github.com/Ak05123/AI-Startup-Idea-Validator-Infosys-Springboard-" target="_blank">
                    📦 GitHub Repository
                </a>
                <a href="#" target="_blank">
                    📄 Documentation
                </a>
                <a href="#" target="_blank">
                    🐛 Report Issue
                </a>
            </div>
            <div style="margin-top: 0.75rem; font-size: 0.7rem; color: rgba(255,255,255,0.2);">
                Built with Streamlit • Python • Plotly
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )