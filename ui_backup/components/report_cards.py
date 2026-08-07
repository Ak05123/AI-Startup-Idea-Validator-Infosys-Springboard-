"""
Report Cards Component - Reusable cards for displaying analysis results.
"""

import streamlit as st
from typing import Any, Dict, List, Optional


def render_article_card(article: Dict[str, Any]) -> None:
    """
    Render an expandable article card.

    Args:
        article: Article data with title, source, date, summary, url
    """
    title = article.get("title", "Untitled")
    source = article.get("source", "Unknown")
    date = article.get("date", "")
    summary = article.get("summary", "")
    url = article.get("url", "")
    relevance = article.get("relevance", 0.5)

    relevance_color = "#00d4aa" if relevance >= 0.8 else "#ffd93d" if relevance >= 0.5 else "#ff6b6b"

    with st.expander(f"📰 {title}", expanded=False):
        st.markdown(
            f"""
            <div style="padding:0.5rem 0;">
                <div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap;margin-bottom:0.75rem;">
                    <span style="font-size:0.8rem;color:#4d94ff;font-weight:500;">{source}</span>
                    <span style="font-size:0.75rem;color:rgba(255,255,255,0.4);">{date}</span>
                    <span style="background:{relevance_color}22;color:{relevance_color};
                        padding:2px 8px;border-radius:12px;font-size:0.7rem;font-weight:500;">
                        {relevance:.0%} relevance
                    </span>
                </div>
                <p style="font-size:0.9rem;color:rgba(255,255,255,0.7);line-height:1.6;">
                    {summary}
                </p>
                {f'<a href="{url}" target="_blank" style="display:inline-block;margin-top:0.75rem;color:#4d94ff;font-size:0.85rem;">🔗 Read full article →</a>' if url else ""}
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_competitor_card(competitor: Dict[str, Any]) -> None:
    """
    Render a competitor card.

    Args:
        competitor: Competitor data with name, description, funding, etc.
    """
    name = competitor.get("name", "Unknown")
    description = competitor.get("description", "")
    funding = competitor.get("funding", "N/A")
    market_share = competitor.get("market_share", 0)
    strength = competitor.get("strength", 0)
    threat = competitor.get("threat_level", "medium")

    threat_colors = {"low": "#00d4aa", "medium": "#ffd93d", "high": "#ff6b6b"}
    threat_color = threat_colors.get(threat.lower(), "#ffd93d")

    st.markdown(
        f"""
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
            border-radius:12px;padding:1.25rem;margin-bottom:0.75rem;
            transition:all 0.3s ease;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                <div>
                    <div style="font-weight:600;font-size:1rem;">{name}</div>
                    <div style="font-size:0.85rem;color:rgba(255,255,255,0.6);margin-top:0.25rem;">
                        {description[:150]}{"..." if len(description) > 150 else ""}
                    </div>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Funding</div>
                    <div style="font-weight:600;color:#4d94ff;">{funding}</div>
                </div>
            </div>
            <div style="display:flex;gap:1rem;margin-top:0.75rem;flex-wrap:wrap;">
                <span style="font-size:0.8rem;color:rgba(255,255,255,0.5);">
                    📊 Market Share: <strong style="color:#fff;">{market_share}%</strong>
                </span>
                <span style="font-size:0.8rem;color:rgba(255,255,255,0.5);">
                    ⭐ Strength: <strong style="color:#fff;">{"⭐" * strength}</strong>
                </span>
                <span style="background:{threat_color}22;color:{threat_color};
                    padding:2px 8px;border-radius:12px;font-size:0.7rem;font-weight:500;">
                    {threat.upper()} THREAT
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_swot_quadrant(
    title: str,
    items: List[str],
    icon: str,
    color: str,
) -> None:
    """
    Render a SWOT quadrant.

    Args:
        title: Quadrant title (Strengths, Weaknesses, etc.)
        items: List of items in the quadrant
        icon: Emoji icon
        color: Accent color
    """
    items_html = "".join(
        f'<div style="padding:0.5rem 0;border-bottom:1px solid rgba(255,255,255,0.05);'
        f'display:flex;align-items:flex-start;gap:0.5rem;">'
        f'<span style="color:{color};font-size:1rem;">▸</span>'
        f'<span style="font-size:0.85rem;color:rgba(255,255,255,0.7);">{item}</span></div>'
        for item in items
    )
    st.markdown(
        f"""
        <div class="swot-quadrant" style="border-color:{color}33;">
            <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.75rem;">
                <span style="font-size:1.5rem;">{icon}</span>
                <span style="font-size:1rem;font-weight:700;color:{color};">{title}</span>
            </div>
            {items_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_pricing_tier(
    tier: Dict[str, Any],
    color: str = "#4d94ff",
    featured: bool = False,
) -> None:
    """
    Render a pricing tier card.

    Args:
        tier: Pricing tier data
        color: Accent color
        featured: Whether this is the featured tier
    """
    features_list = "".join(
        f'<div style="padding:0.3rem 0;font-size:0.8rem;color:rgba(255,255,255,0.6);'
        f'display:flex;align-items:center;gap:0.5rem;">'
        f'<span style="color:{color};">✓</span> {f}</div>'
        for f in tier.get("features", [])
    )

    st.markdown(
        f"""
        <div class="pricing-card{' featured' if featured else ''}"
             style="border-color:{color}44;">
            <div style="font-size:2rem;margin-bottom:0.25rem;">{tier.get("icon", "⭐")}</div>
            <div style="font-size:1.1rem;font-weight:700;color:{color};">
                {tier.get("tier", "")}
            </div>
            <div style="font-size:1.75rem;font-weight:800;margin:0.75rem 0;">
                {tier.get("price", "")}
            </div>
            <div style="text-align:left;padding-top:0.75rem;border-top:1px solid rgba(255,255,255,0.1);">
                {features_list}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_item(feature: Dict[str, Any]) -> None:
    """
    Render a prioritized feature item.

    Args:
        feature: Feature data with name, priority, complexity, impact
    """
    priority_colors = {"P0": "#ff6b6b", "P1": "#ffd93d", "P2": "#4d94ff"}
    p = feature.get("priority", "P2")
    color = priority_colors.get(p, "#4d94ff")

    st.markdown(
        f"""
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;padding:1rem;margin-bottom:0.5rem;border-left:4px solid {color};">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <div>
                    <div style="font-weight:600;font-size:0.95rem;">{feature.get("feature", "")}</div>
                    <div style="display:flex;gap:1rem;margin-top:0.25rem;">
                        <span style="font-size:0.8rem;color:{color};font-weight:500;">
                            {p} Priority
                        </span>
                        <span style="font-size:0.8rem;color:rgba(255,255,255,0.5);">
                            📊 {feature.get("complexity", "")} Complexity
                        </span>
                    </div>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Impact</div>
                    <div style="font-size:1rem;">{"⭐" * feature.get("impact", 0)}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )