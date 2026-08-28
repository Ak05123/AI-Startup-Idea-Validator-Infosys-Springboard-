"""
Footer Component - Premium footer with links and branding.
"""

import streamlit as st


def render_footer() -> None:
    """
    Render the application footer with branding and links.
    """
    st.markdown(
        """
        <div class="footer">
            <div class="footer-text">
                © 2026 AI Startup Idea Validator — Infosys Springboard Virtual Internship
            </div>
            <div class="footer-links">
                <a href="https://github.com/Ak05123/AI-Startup-Idea-Validator-Infosys-Springboard-"
                   target="_blank">GitHub</a>
                <a href="#" onclick="return false;">Documentation</a>
                <a href="#" onclick="return false;">Privacy Policy</a>
                <a href="#" onclick="return false;">Terms of Service</a>
            </div>
            <div style="font-size:0.7rem;color:rgba(255,255,255,0.2);margin-top:0.75rem;">
                Built with Streamlit • Multi-Agent AI Architecture • v2.0.0
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )