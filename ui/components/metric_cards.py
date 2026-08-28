"""
Metric Cards Component - Reusable metric display cards with glassmorphism.
"""

import streamlit as st
from typing import List, Optional, Tuple


def render_metric_card(
    icon: str,
    label: str,
    value: str,
    delta: Optional[str] = None,
    color: str = "#4d94ff",
) -> None:
    """
    Render a single metric card.

    Args:
        icon: Emoji icon
        label: Metric label
        value: Metric value
        delta: Optional change indicator
        color: Accent color for the card
    """
    delta_html = f'<div style="font-size:0.8rem;color:#00d4aa;margin-top:0.15rem;">{delta}</div>' if delta else ""
    st.markdown(
        f"""
        <div style="text-align:center;padding:1.25rem;background:rgba(255,255,255,0.03);
            border:1px solid rgba(255,255,255,0.08);border-radius:12px;
            transition:all 0.3s ease;height:100%;">
            <div style="font-size:1.5rem;margin-bottom:0.5rem;">{icon}</div>
            <div style="font-size:1.5rem;font-weight:700;color:{color};">
                {value}
            </div>
            <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);margin-top:0.25rem;">
                {label}
            </div>
            {delta_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric_row(
    metrics: List[Tuple[str, str, str, str]],
    columns: int = 4,
) -> None:
    """
    Render a row of metric cards.

    Args:
        metrics: List of (icon, label, value, delta) tuples
        columns: Number of columns (default 4)
    """
    cols = st.columns(min(columns, len(metrics)))
    for i, (icon, label, value, delta) in enumerate(metrics):
        with cols[i % columns]:
            render_metric_card(icon, label, value, delta)


def render_score_circle(
    score: float,
    label: str,
    max_score: float = 100.0,
    size: int = 120,
) -> None:
    """
    Render a circular score gauge.

    Args:
        score: Current score value
        label: Label for the score
        max_score: Maximum possible score
        size: Diameter of the circle in pixels
    """
    percentage = (score / max_score) * 100
    color = "#00d4aa" if percentage >= 70 else "#ffd93d" if percentage >= 40 else "#ff6b6b"
    degrees = int((percentage / 100) * 360)

    st.markdown(
        f"""
        <div style="text-align:center;padding:1rem;">
            <div style="width:{size}px;height:{size}px;border-radius:50%;margin:0 auto;
                background:conic-gradient({color} 0deg {degrees}deg, rgba(255,255,255,0.1) {degrees}deg 360deg);
                display:flex;align-items:center;justify-content:center;flex-direction:column;">
                <div style="font-size:1.75rem;font-weight:700;color:{color};">{score:.0f}</div>
                <div style="font-size:0.65rem;color:rgba(255,255,255,0.5);">/ {max_score:.0f}</div>
            </div>
            <div style="font-size:0.85rem;color:rgba(255,255,255,0.6);margin-top:0.5rem;font-weight:500;">
                {label}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_confidence_gauge(confidence: float, label: str = "Confidence") -> None:
    """
    Render a confidence gauge with color coding.

    Args:
        confidence: Confidence percentage (0-100)
        label: Label for the gauge
    """
    color = "#00d4aa" if confidence >= 70 else "#ffd93d" if confidence >= 40 else "#ff6b6b"
    level = "Very High" if confidence >= 90 else "High" if confidence >= 75 else "Moderate" if confidence >= 60 else "Low"

    st.markdown(
        f"""
        <div style="text-align:center;padding:1.5rem;background:rgba(255,255,255,0.03);
            border:1px solid rgba(255,255,255,0.08);border-radius:12px;">
            <div style="width:100px;height:100px;border-radius:50%;margin:0 auto;
                background:conic-gradient({color} 0deg {int(confidence*3.6)}deg, rgba(255,255,255,0.1) {int(confidence*3.6)}deg 360deg);
                display:flex;align-items:center;justify-content:center;flex-direction:column;">
                <div style="font-size:1.5rem;font-weight:700;color:{color};">{confidence:.0f}%</div>
            </div>
            <div style="font-size:0.9rem;color:{color};font-weight:600;margin-top:0.5rem;">{level}</div>
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.5);">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )