"""
Card components for the AI Startup Idea Validator.
"""

import streamlit as st
from typing import Any, Dict, List, Optional

from utils.helpers import calculate_sentiment_color, get_relevance_badge


def render_article_card(article: Dict[str, Any]) -> None:
    """Render a beautiful article card."""
    sentiment_color = calculate_sentiment_color(article.get("sentiment", "neutral"))
    
    st.markdown(
        f"""
        <div class="article-card animate-fade-in">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <div class="article-title">{article['title']}</div>
                    <div style="display: flex; gap: 1rem; align-items: center; margin-top: 0.4rem;">
                        <span class="article-source">📰 {article.get('source', 'Unknown')}</span>
                        <span class="article-date">📅 {article.get('date', '')}</span>
                        <span style="color: {sentiment_color}; font-size: 0.75rem; padding: 2px 8px; border-radius: 12px; background: {sentiment_color}22;">
                            {article.get('sentiment', 'neutral').title()}
                        </span>
                    </div>
                </div>
                <div>{get_relevance_badge(article.get('relevance', 0))}</div>
            </div>
            <div class="article-summary">{article.get('summary', '')}</div>
            <div class="article-meta">
                {''.join(f'<span class="status-badge info">#{kw}</span>' for kw in article.get('keywords', []))}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_competitor_card(competitor: Dict[str, Any], rank: int = 0) -> None:
    """Render a competitor card with strength rating."""
    threat = competitor.get("threat_level", "medium")
    threat_colors = {"high": "#ff6b6b", "medium": "#ffd93d", "low": "#00d4aa"}
    threat_color = threat_colors.get(threat, "#ffd93d")
    
    stars = "⭐" * competitor.get("strength", 0)
    
    st.markdown(
        f"""
        <div class="glass-card animate-fade-in-up" style="margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <div style="display: flex; align-items: center; gap: 0.75rem;">
                        <span style="font-size: 1.5rem;">🏢</span>
                        <div>
                            <div style="font-size: 1.1rem; font-weight: 600;">{competitor.get('name', 'Unknown')}</div>
                            <div style="font-size: 0.8rem; color: rgba(255,255,255,0.5);">{stars}</div>
                        </div>
                    </div>
                    <div style="font-size: 0.85rem; color: rgba(255,255,255,0.6); margin-top: 0.75rem;">
                        {competitor.get('description', '')}
                    </div>
                </div>
                <span style="background: {threat_color}22; color: {threat_color}; padding: 2px 12px; border-radius: 12px; font-size: 0.75rem; font-weight: 500;">
                    {threat.title()} Threat
                </span>
            </div>
            <div style="margin-top: 1rem; display: flex; gap: 1rem; flex-wrap: wrap;">
                <div style="font-size: 0.8rem; color: rgba(255,255,255,0.5);">💰 {competitor.get('funding', 'N/A')}</div>
                <div style="font-size: 0.8rem; color: rgba(255,255,255,0.5);">📊 {competitor.get('market_share', 0)}% Market Share</div>
                {f'<div style="font-size: 0.8rem; color: rgba(255,255,255,0.5);">📅 Founded {competitor.get("founded", "N/A")}</div>' if competitor.get('founded') else ''}
                {f'<div style="font-size: 0.8rem; color: rgba(255,255,255,0.5);">👥 {competitor.get("employees", "N/A")} employees</div>' if competitor.get('employees') else ''}
            </div>
            <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem; flex-wrap: wrap;">
                {''.join(f'<span class="status-badge info">{feat}</span>' for feat in competitor.get('key_features', []))}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_funding_card(funding: Dict[str, Any]) -> None:
    """Render a funding news card."""
    investors_str = ", ".join(funding.get("investors", []))
    
    st.markdown(
        f"""
        <div class="glass-card animate-fade-in" style="margin-bottom: 0.75rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: rgba(255,255,255,0.7);">
                        {funding.get('round', 'Round')}
                    </div>
                    <div style="font-size: 1.1rem; font-weight: 700; margin-top: 0.25rem;">
                        {funding.get('company', 'Unknown')}
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 1.25rem; font-weight: 700; color: #00d4aa;">
                        {funding.get('amount', 'N/A')}
                    </div>
                    <div style="font-size: 0.75rem; color: rgba(255,255,255,0.4);">
                        {funding.get('date', '')}
                    </div>
                </div>
            </div>
            <div style="margin-top: 0.75rem; font-size: 0.85rem; color: rgba(255,255,255,0.5);">
                🎯 {funding.get('focus', '')}
            </div>
            <div style="margin-top: 0.5rem; font-size: 0.8rem; color: rgba(255,255,255,0.4);">
                👥 Investors: {investors_str}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_discussion_card(discussion: Dict[str, Any]) -> None:
    """Render a customer discussion card."""
    sentiment_color = calculate_sentiment_color(discussion.get("sentiment", "neutral"))
    
    st.markdown(
        f"""
        <div class="glass-card animate-fade-in" style="margin-bottom: 0.75rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="font-size: 0.85rem; font-weight: 600; color: rgba(255,255,255,0.6);">
                    💬 {discussion.get('platform', 'Unknown Platform')}
                </div>
                <div style="display: flex; gap: 1rem; align-items: center;">
                    <span style="font-size: 0.8rem; color: rgba(255,255,255,0.4);">
                        🔥 {discussion.get('engagement', 0)} engagements
                    </span>
                    <span style="color: {sentiment_color}; font-size: 0.75rem;">
                        {discussion.get('sentiment', 'neutral').title()}
                    </span>
                </div>
            </div>
            <div style="font-size: 1rem; font-weight: 600; margin-top: 0.5rem;">
                {discussion.get('title', '')}
            </div>
            <div style="font-size: 0.8rem; color: rgba(255,255,255,0.4); margin-top: 0.5rem;">
                {discussion.get('date', '')}
            </div>
            <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem; flex-wrap: wrap;">
                {''.join(f'<span class="status-badge warning">{point}</span>' for point in discussion.get('key_points', []))}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_report_card(report: Dict[str, Any]) -> None:
    """Render an industry report card."""
    st.markdown(
        f"""
        <div class="glass-card animate-fade-in" style="margin-bottom: 0.75rem;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <div style="font-size: 1rem; font-weight: 600;">{report.get('title', '')}</div>
                    <div style="font-size: 0.8rem; color: rgba(255,255,255,0.5); margin-top: 0.3rem;">
                        📚 {report.get('publisher', 'Unknown')} — 📅 {report.get('date', '')}
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 1.1rem; font-weight: 700; color: #4d94ff;">
                        {report.get('market_size', 'N/A')}
                    </div>
                    <div style="font-size: 0.75rem; color: #00d4aa;">
                        📈 {report.get('growth_rate', 'N/A')} CAGR
                    </div>
                </div>
            </div>
            <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem; flex-wrap: wrap;">
                {''.join(f'<span class="status-badge success">{finding}</span>' for finding in report.get('key_findings', []))}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_card(icon: str, title: str, description: str) -> None:
    """Render a feature card for the home page."""
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_insight_card(title: str, items: List[str], icon: str = "💡", color: str = "#4d94ff") -> None:
    """Render an AI insight card for the right panel."""
    items_html = "".join(
        f'<div style="font-size: 0.85rem; color: rgba(255,255,255,0.7); padding: 0.3rem 0; display: flex; align-items: center; gap: 0.5rem;">'
        f'<span style="color: {color};">▸</span> {item}</div>'
        for item in items
    )
    
    st.markdown(
        f"""
        <div class="insight-card">
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
                <span style="font-size: 1.25rem;">{icon}</span>
                <span style="font-size: 0.9rem; font-weight: 600;">{title}</span>
            </div>
            {items_html}
        </div>
        """,
        unsafe_allow_html=True,
    )