"""
Hero Section Component - Premium landing page hero with glassmorphism.
"""

import streamlit as st
from typing import List, Tuple


def render_hero_section() -> None:
    """
    Render the premium hero section with title, subtitle, and stats.
    """
    st.markdown(
        """
        <div class="hero-section">
            <div style="position:relative;z-index:1;">
                <div style="font-size:4rem;margin-bottom:1rem;">🚀</div>
                <h1 class="hero-title">AI Startup Idea Validator</h1>
                <p class="hero-subtitle">
                    Validate startup ideas using AI-powered Multi-Agent Intelligence.
                    Make data-driven decisions with comprehensive market analysis.
                </p>
                <div class="hero-stats">
                    <div class="hero-stat">
                        <div class="hero-stat-value">10+</div>
                        <div class="hero-stat-label">Sources Analyzed</div>
                    </div>
                    <div class="hero-stat">
                        <div class="hero-stat-value">87%</div>
                        <div class="hero-stat-label">Confidence Score</div>
                    </div>
                    <div class="hero-stat">
                        <div class="hero-stat-value">3s</div>
                        <div class="hero-stat-label">Analysis Time</div>
                    </div>
                    <div class="hero-stat">
                        <div class="hero-stat-value">9</div>
                        <div class="hero-stat-label">AI Agents</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(
    icon: str,
    title: str,
    subtitle: str,
    breadcrumb: str = "",
) -> None:
    """
    Render a page header with icon, title, and subtitle.

    Args:
        icon: Emoji icon for the page
        title: Page title
        subtitle: Page subtitle/description
        breadcrumb: Optional breadcrumb text
    """
    if breadcrumb:
        st.markdown(
            f'<div class="breadcrumb">{breadcrumb}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div style="margin-bottom:2rem;">
            <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.5rem;">
                <span style="font-size:2rem;">{icon}</span>
                <h1 style="font-size:2rem;font-weight:800;margin:0;
                    background:linear-gradient(135deg,#fff 0%,#4d94ff 50%,#00d4aa 100%);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
                    {title}
                </h1>
            </div>
            <p style="font-size:1rem;color:rgba(255,255,255,0.6);margin-left:2.75rem;">
                {subtitle}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_startup_info_header() -> None:
    """
    Render the current startup info header bar.
    Shows name, idea preview, industry, and country from session state.
    """
    startup_idea = st.session_state.get("startup_idea", "")
    industry = st.session_state.get("industry", "")
    country = st.session_state.get("country", "")

    if not startup_idea:
        return

    st.markdown(
        f"""
        <div class="startup-info-header">
            <div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap;">
                <span style="font-size:1.5rem;">💡</span>
                <span style="font-weight:700;font-size:1.1rem;">Startup Idea</span>
                <span style="color:rgba(255,255,255,0.4);">|</span>
                <span style="color:#4d94ff;">{industry or "N/A"}</span>
                <span style="color:rgba(255,255,255,0.4);">|</span>
                <span style="color:#00d4aa;">{country or "N/A"}</span>
                <span style="color:rgba(255,255,255,0.4);">|</span>
                <span style="color:rgba(255,255,255,0.6);font-size:0.9rem;">
                    {startup_idea[:120]}{"..." if len(startup_idea) > 120 else ""}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
