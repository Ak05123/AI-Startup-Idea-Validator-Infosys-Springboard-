"""
Metric display components for the AI Startup Idea Validator.
"""

import streamlit as st
from typing import List, Tuple, Optional


def render_metric_row(metrics: List[Tuple[str, str, Optional[str], str]]) -> None:
    """
    Render a row of metric cards.

    Args:
        metrics: List of tuples (label, value, delta, icon)
    """
    cols = st.columns(len(metrics))
    
    for i, (label, value, delta, icon) in enumerate(metrics):
        with cols[i]:
            delta_html = f'<div class="metric-delta">{delta}</div>' if delta else ""
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-content">
                        <div class="metric-label">{label}</div>
                        <div class="metric-value">{value}</div>
                        {delta_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_confidence_gauge(score: int, label: str = "Confidence Score") -> None:
    """
    Render a circular confidence gauge.

    Args:
        score: Confidence score (0-100)
        label: Label for the gauge
    """
    # Calculate color based on score
    if score >= 80:
        color = "#00d4aa"
    elif score >= 60:
        color = "#ffd93d"
    else:
        color = "#ff6b6b"
    
    # Calculate conic gradient degrees
    degrees = (score / 100) * 360
    
    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center; padding: 1.5rem;">
            <div style="
                width: 120px;
                height: 120px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
                background: conic-gradient({color} 0deg {degrees}deg, rgba(255,255,255,0.05) {degrees}deg 360deg);
                position: relative;
            ">
                <div style="
                    position: absolute;
                    width: 90px;
                    height: 90px;
                    border-radius: 50%;
                    background: #0a0a1a;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-direction: column;
                ">
                    <div style="font-size: 1.75rem; font-weight: 700; color: {color};">{score}%</div>
                    <div style="font-size: 0.65rem; color: rgba(255,255,255,0.5);">{label}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stat_row(stats: List[Tuple[str, str]]) -> None:
    """
    Render a row of simple statistics.

    Args:
        stats: List of tuples (label, value)
    """
    cols = st.columns(len(stats))
    
    for i, (label, value) in enumerate(stats):
        with cols[i]:
            st.markdown(
                f"""
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 1.5rem; font-weight: 700; color: #4d94ff;">{value}</div>
                    <div style="font-size: 0.75rem; color: rgba(255,255,255,0.5); margin-top: 0.25rem;">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_progress_indicator(current: int, total: int, label: str = "Progress") -> None:
    """
    Render a progress indicator with percentage.

    Args:
        current: Current step
        total: Total steps
        label: Label for the progress
    """
    percentage = int((current / total) * 100) if total > 0 else 0
    
    st.markdown(
        f"""
        <div style="margin: 1rem 0;">
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 0.5rem;">
                <span style="color: rgba(255,255,255,0.6);">{label}</span>
                <span style="color: #4d94ff; font-weight: 600;">{percentage}%</span>
            </div>
            <div style="height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden;">
                <div style="
                    height: 100%;
                    width: {percentage}%;
                    background: linear-gradient(135deg, #0066ff 0%, #00d4aa 100%);
                    border-radius: 3px;
                    transition: width 0.5s ease;
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )