"""
Shared page utilities for consistent enterprise-grade page structure.
All pages use these components for standardized layout.
"""

import streamlit as st
from typing import List, Tuple, Optional


def navigate_to(page: str) -> None:
    """Navigate to a Streamlit page using switch_page."""
    st.switch_page(f"pages/{page}")


def render_breadcrumb(page_name: str) -> None:
    """Render breadcrumb navigation."""
    st.markdown(
        f"""
        <div style="display:flex;align-items:center;gap:0.5rem;padding:0.5rem 0;margin-bottom:1rem;">
            <a href="#" onclick="document.querySelector('.st-emotion-cache-1avcm0n a').click()" 
               style="color:rgba(255,255,255,0.4);text-decoration:none;font-size:0.85rem;transition:color 0.2s;"
               onmouseover="this.style.color='#4d94ff'" onmouseout="this.style.color='rgba(255,255,255,0.4)'">🏠 Home</a>
            <span style="color:rgba(255,255,255,0.2);font-size:0.85rem;">›</span>
            <span style="color:#4d94ff;font-size:0.85rem;font-weight:500;">{page_name}</span>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 11])
    with col1:
        if st.button("◀", key=f"back_{page_name}", help="Back to Home"):
            navigate_to("01_Home.py")


def render_hero(icon: str, title: str, subtitle: str, description: str) -> None:
    """Render a professional hero banner."""
    st.markdown(
        f"""
        <div style="text-align:center;padding:2.5rem 2rem;margin-bottom:1.5rem;
            background:linear-gradient(135deg,#0a0a1a 0%,#1a1a3e 50%,#0a0a1a 100%);
            border-radius:16px;position:relative;overflow:hidden;">
            <div style="position:absolute;top:0;left:0;right:0;bottom:0;
                background:radial-gradient(circle at 50% 50%,rgba(0,102,255,0.1) 0%,transparent 50%);pointer-events:none;"></div>
            <div style="position:relative;z-index:1;">
                <div style="font-size:2.5rem;margin-bottom:0.75rem;">{icon}</div>
                <h1 style="font-size:2.2rem;font-weight:800;
                    background:linear-gradient(135deg,#fff 0%,#4d94ff 50%,#00d4aa 100%);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                    background-clip:text;margin-bottom:0.5rem;line-height:1.2;">{title}</h1>
                <p style="font-size:1.05rem;color:rgba(255,255,255,0.7);max-width:700px;margin:0 auto 0.75rem;line-height:1.6;">{subtitle}</p>
                <p style="font-size:0.9rem;color:rgba(255,255,255,0.5);max-width:800px;margin:0 auto;line-height:1.7;">{description}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_section(title: str, subtitle: str = "") -> None:
    """Render a section header."""
    sub = f'<p style="font-size:0.9rem;color:rgba(255,255,255,0.5);">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f'<div style="margin:1.5rem 0 1rem;"><h2 style="font-size:1.5rem;font-weight:700;">{title}</h2>{sub}</div>',
        unsafe_allow_html=True)


def render_card(icon: str, title: str, content: str, color: str = "#4d94ff") -> None:
    """Render a glass card."""
    st.markdown(
        f"""
        <div style="background:rgba(255,255,255,0.03);backdrop-filter:blur(20px);
            border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.25rem;
            transition:all 0.3s ease;margin-bottom:0.75rem;"
            onmouseover="this.style.background='rgba(255,255,255,0.06)';this.style.borderColor='rgba(255,255,255,0.15)';this.style.transform='translateY(-2px)'"
            onmouseout="this.style.background='rgba(255,255,255,0.03)';this.style.borderColor='rgba(255,255,255,0.08)';this.style.transform='translateY(0)'">
            <div style="display:flex;align-items:flex-start;gap:0.75rem;">
                <span style="font-size:1.5rem;flex-shrink:0;">{icon}</span>
                <div>
                    <div style="font-weight:600;font-size:0.95rem;color:rgba(255,255,255,0.9);">{title}</div>
                    <div style="font-size:0.85rem;color:rgba(255,255,255,0.55);margin-top:0.25rem;line-height:1.6;">{content}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_workflow(steps: List[Tuple[str, str, str]]) -> None:
    """Render a vertical workflow diagram."""
    html = '<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1.5rem;margin:1rem 0;">'
    html += '<div style="font-size:1rem;font-weight:600;margin-bottom:1rem;text-align:center;">⚡ Workflow Pipeline</div>'
    html += '<div style="display:flex;flex-direction:column;align-items:center;gap:0.25rem;">'
    
    for i, (icon, label, desc) in enumerate(steps):
        is_last = i == len(steps) - 1
        html += f"""
        <div style="display:flex;align-items:center;gap:0.75rem;width:100%;max-width:500px;
            background:rgba(0,102,255,0.05);border:1px solid rgba(0,102,255,0.15);
            border-radius:10px;padding:0.75rem 1rem;transition:all 0.3s ease;"
            onmouseover="this.style.background='rgba(0,102,255,0.1)'"
            onmouseout="this.style.background='rgba(0,102,255,0.05)'">
            <div style="font-size:1.3rem;width:2rem;text-align:center;">{icon}</div>
            <div style="flex:1;">
                <div style="font-weight:600;font-size:0.85rem;">{label}</div>
                <div style="font-size:0.75rem;color:rgba(255,255,255,0.45);">{desc}</div>
            </div>
        </div>
        """
        if not is_last:
            html += '<div style="color:rgba(0,102,255,0.3);font-size:1rem;">↓</div>'
    
    html += '</div></div>'
    st.markdown(html, unsafe_allow_html=True)


def render_tech_badges(techs: List[Tuple[str, str]]) -> None:
    """Render technology badges."""
    html = '<div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin:0.75rem 0;">'
    for icon, name in techs:
        html += f'<span style="background:rgba(0,102,255,0.1);border:1px solid rgba(0,102,255,0.2);border-radius:20px;padding:0.3rem 0.75rem;font-size:0.8rem;display:flex;align-items:center;gap:0.35rem;">{icon} {name}</span>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def render_table(headers: List[str], rows: List[List[str]]) -> None:
    """Render a professional table."""
    header_html = "".join(f'<th style="padding:0.6rem 0.75rem;text-align:left;font-size:0.8rem;color:rgba(255,255,255,0.5);border-bottom:1px solid rgba(255,255,255,0.1);font-weight:500;">{h}</th>' for h in headers)
    rows_html = ""
    for row in rows:
        rows_html += "<tr>" + "".join(f'<td style="padding:0.6rem 0.75rem;font-size:0.85rem;color:rgba(255,255,255,0.7);border-bottom:1px solid rgba(255,255,255,0.05);">{c}</td>' for c in row) + "</tr>"
    
    st.markdown(
        f"""
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:0.75rem;margin:0.75rem 0;overflow-x:auto;">
            <table style="width:100%;border-collapse:collapse;">{header_html}{rows_html}</table>
        </div>
        """, unsafe_allow_html=True)


def render_advantages(items: List[Tuple[str, str, str]]) -> None:
    """Render advantages in a grid."""
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(items):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style="background:rgba(0,212,170,0.03);border:1px solid rgba(0,212,170,0.12);border-radius:12px;padding:1.25rem;text-align:center;height:100%;">
                    <div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div>
                    <div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">{title}</div>
                    <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{desc}</div>
                </div>
                """, unsafe_allow_html=True)


def render_challenges(items: List[Tuple[str, str, str]]) -> None:
    """Render challenges in a grid."""
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(items):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style="background:rgba(255,107,107,0.03);border:1px solid rgba(255,107,107,0.12);border-radius:12px;padding:1.25rem;text-align:center;height:100%;">
                    <div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div>
                    <div style="font-weight:600;font-size:0.9rem;margin-bottom:0.25rem;">{title}</div>
                    <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">{desc}</div>
                </div>
                """, unsafe_allow_html=True)


def render_faqs(faqs: List[Tuple[str, str]]) -> None:
    """Render FAQ expanders."""
    render_section("❓ Frequently Asked Questions")
    for i, (q, a) in enumerate(faqs):
        with st.expander(f"📌 {q}", expanded=False):
            st.markdown(f'<div style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">{a}</div>', unsafe_allow_html=True)


def render_summary(title: str, content: str) -> None:
    """Render a professional summary/conclusion."""
    st.markdown(
        f"""
        <div style="background:linear-gradient(135deg,rgba(0,102,255,0.08),rgba(0,212,170,0.08));
            border:1px solid rgba(0,102,255,0.2);border-radius:12px;padding:1.5rem;margin:1.5rem 0;">
            <div style="font-size:1.1rem;font-weight:600;margin-bottom:0.5rem;">{title}</div>
            <div style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.7;">{content}</div>
        </div>
        """, unsafe_allow_html=True)


def render_page_footer() -> None:
    """Render back to home button and footer."""
    st.markdown('<hr style="border-color:rgba(255,255,255,0.08);margin:2rem 0;">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            navigate_to("01_Home.py")
    
    from components.footer import render_footer
    render_footer()