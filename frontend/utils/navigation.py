"""
Navigation utilities for the AI Startup Idea Validator.
Provides breadcrumb navigation, page routing, and back buttons.
"""

import streamlit as st
from typing import List, Tuple, Optional


# Page registry for navigation
PAGE_REGISTRY = {
    "Home": {"title": "Home", "icon": "🏠"},
    "Web_Search_Agent": {"title": "Web Search Agent", "icon": "🌐"},
    "Market_Analysis": {"title": "Market Analysis", "icon": "📈"},
    "Competitor_Analysis": {"title": "Competitor Analysis", "icon": "🏆"},
    "SWOT": {"title": "SWOT Analysis", "icon": "⚠️"},
    "MVP": {"title": "MVP Recommendation", "icon": "💡"},
    "GTM": {"title": "GTM Strategy", "icon": "📢"},
    "Report": {"title": "Final Report", "icon": "📄"},
    "AI_Advisor": {"title": "AI Advisor", "icon": "🤖"},
    "Orchestrator": {"title": "Multi-Agent AI", "icon": "🤖"},
    "Settings": {"title": "Settings", "icon": "⚙️"},
    "Market_Intelligence": {"title": "Market Intelligence", "icon": "📊"},
    "Actionable_Reports": {"title": "Actionable Reports", "icon": "📋"},
    "Deep_Web_Search": {"title": "Deep Web Search", "icon": "🔍"},
    "Beautiful_Charts": {"title": "Charts & Visualizations", "icon": "📉"},
}


def navigate_to(page_key: str) -> None:
    """Navigate to a page by setting session state."""
    st.session_state.current_page = page_key
    st.rerun()


def render_breadcrumbs(current_page: str) -> None:
    """
    Render breadcrumb navigation with Home > Current Page.

    Args:
        current_page: The key of the current page
    """
    page_info = PAGE_REGISTRY.get(current_page, {})
    page_title = page_info.get("title", current_page)
    page_icon = page_info.get("icon", "📄")

    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 0; margin-bottom: 0.5rem;">
            <a href="#" onclick="alert('Navigating home...')" 
               style="color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.85rem; 
                      transition: color 0.2s; cursor: pointer;"
               onmouseover="this.style.color='#4d94ff'" 
               onmouseout="this.style.color='rgba(255,255,255,0.4)'"
               id="breadcrumb-home">
               🏠 Home
            </a>
            <span style="color: rgba(255,255,255,0.2); font-size: 0.85rem;">›</span>
            <span style="color: #4d94ff; font-size: 0.85rem; font-weight: 500;">
                {page_icon} {page_title}
            </span>
        </div>

        <script>
        document.getElementById('breadcrumb-home')?.addEventListener('click', function(e) {{
            e.preventDefault();
            // Streamlit will handle this via the button below
        }});
        </script>
        """,
        unsafe_allow_html=True,
    )

    # Hidden Streamlit button for actual navigation
    col1, col2 = st.columns([1, 10])
    with col1:
        if st.button("◀", key="back_home_btn", help="Back to Home"):
            navigate_to("Home")


def render_hero_section(
    icon: str,
    title: str,
    subtitle: str,
    description: str,
) -> None:
    """
    Render a professional hero section for any page.

    Args:
        icon: Emoji or icon for the page
        title: Page title
        subtitle: Page subtitle
        description: Longer description
    """
    st.markdown(
        f"""
        <div class="hero-section" style="padding: 2rem 2rem; margin-bottom: 1.5rem;">
            <div style="position: relative; z-index: 1;">
                <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">{icon}</div>
                <h1 style="font-size: 2.5rem; font-weight: 800; 
                    background: linear-gradient(135deg, #ffffff 0%, #4d94ff 50%, #00d4aa 100%);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                    background-clip: text; margin-bottom: 0.5rem; line-height: 1.2;">
                    {title}
                </h1>
                <p style="font-size: 1.1rem; color: rgba(255,255,255,0.7); max-width: 700px; 
                          margin: 0 auto 1rem; line-height: 1.6;">
                    {subtitle}
                </p>
                <p style="font-size: 0.9rem; color: rgba(255,255,255,0.5); max-width: 800px; 
                          margin: 0 auto; line-height: 1.7;">
                    {description}
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(title: str, subtitle: str = "") -> None:
    """Render a section header with title and optional subtitle."""
    subtitle_html = f'<p class="section-subtitle">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f"""
        <div class="section-header">
            <h2 class="section-title">{title}</h2>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_workflow_diagram(steps: List[Tuple[str, str, str]]) -> None:
    """
    Render an animated workflow diagram.

    Args:
        steps: List of (icon, label, description) tuples
    """
    st.markdown(
        """
        <div class="glass-card" style="margin: 1.5rem 0; padding: 2rem;">
            <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 1.5rem; text-align: center;">
                ⚡ Workflow
            </div>
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; align-items: center;">
        """,
        unsafe_allow_html=True,
    )

    for i, (icon, label, desc) in enumerate(steps):
        is_last = i == len(steps) - 1
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <div style="
                    display: flex; flex-direction: column; align-items: center; gap: 0.25rem;
                    padding: 1rem 1.25rem; background: rgba(0,102,255,0.08); 
                    border: 1px solid rgba(0,102,255,0.2); border-radius: 12px;
                    transition: all 0.3s ease; min-width: 120px;
                " class="animate-fade-in">
                    <div style="font-size: 1.5rem;">{icon}</div>
                    <div style="font-size: 0.75rem; font-weight: 600; text-align: center; color: rgba(255,255,255,0.9);">
                        {label}
                    </div>
                    <div style="font-size: 0.65rem; color: rgba(255,255,255,0.4); text-align: center; display: none;">
                        {desc}
                    </div>
                </div>
                {'' if is_last else '<span style="color: rgba(0,102,255,0.4); font-size: 1.2rem;">→</span>'}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div></div>", unsafe_allow_html=True)


def render_faqs(faqs: List[Tuple[str, str]]) -> None:
    """
    Render FAQ expanders.

    Args:
        faqs: List of (question, answer) tuples
    """
    render_section_header("❓ Frequently Asked Questions", "Common questions about this feature")
    
    for i, (question, answer) in enumerate(faqs):
        with st.expander(f"📌 {question}", expanded=False):
            st.markdown(answer)


def render_page_footer() -> None:
    """Render back to home button and footer at bottom of every page."""
    st.markdown('<hr class="gradient-divider">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            navigate_to("Home")
    
    from components.footer import render_footer
    render_footer()