"""
Utility functions for the AI Startup Idea Validator frontend.
"""

import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
import streamlit as st


def load_json(filename: str) -> Dict[str, Any]:
    """
    Load JSON data from the mock_data directory.

    Args:
        filename: Name of the JSON file (e.g., 'search_results.json')

    Returns:
        Parsed JSON data as a dictionary
    """
    mock_dir = Path(__file__).parent.parent / "mock_data"
    filepath = mock_dir / filename

    if not filepath.exists():
        st.error(f"Data file not found: {filepath}")
        return {}

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def get_search_results() -> Dict[str, Any]:
    """Load and return search results mock data."""
    return load_json("search_results.json")


def get_competitor_data() -> Dict[str, Any]:
    """Load and return competitor analysis mock data."""
    return load_json("competitors.json")


def get_market_data() -> Dict[str, Any]:
    """Load and return market analysis mock data."""
    return load_json("market.json")


def format_currency(value: float) -> str:
    """Format a number as a currency string."""
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.1f}B"
    if value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"${value / 1_000:.1f}K"
    return f"${value:.0f}"


def format_percentage(value: float) -> str:
    """Format a number as a percentage string."""
    return f"{value:.1f}%"


def calculate_sentiment_color(sentiment: str) -> str:
    """Return a color based on sentiment value."""
    colors = {
        "positive": "#00d4aa",
        "negative": "#ff6b6b",
        "neutral": "#ffd93d",
        "mixed": "#ff9f43",
    }
    return colors.get(sentiment.lower(), "#ffffff")


def get_relevance_badge(relevance: float) -> str:
    """Generate HTML for a relevance badge."""
    color = "#00d4aa" if relevance >= 0.8 else "#ffd93d" if relevance >= 0.5 else "#ff6b6b"
    return f'<span style="background:{color}33; color:{color}; padding:2px 8px; border-radius:12px; font-size:0.75rem;">{relevance:.0%}</span>'


def simulate_agent_workflow(stage_callback, stages: List[str]) -> None:
    """
    Simulate an AI agent workflow with realistic timing.

    Args:
        stage_callback: Function to call with current stage info
        stages: List of stage names to simulate
    """
    import random

    for i, stage in enumerate(stages):
        # Calculate progress
        progress = (i + 1) / len(stages)

        # Simulate variable processing time
        delay = random.uniform(0.3, 0.8)
        time.sleep(delay)

        # Call callback with stage info
        stage_callback(stage, progress)


def df_to_csv_string(df: pd.DataFrame) -> str:
    """Convert DataFrame to CSV string."""
    return df.to_csv(index=False)


def dict_to_json_string(data: Any) -> str:
    """Convert dictionary to formatted JSON string."""
    return json.dumps(data, indent=2, default=str)


def get_download_link(data: str, filename: str, label: str) -> str:
    """
    Generate an HTML download link.

    Args:
        data: String data to download
        filename: Name of the file
        label: Display label for the link

    Returns:
        HTML string with download link
    """
    import base64

    b64 = base64.b64encode(data.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}" class="download-button">{label}</a>'


def create_metric_card_html(
    label: str, value: str, delta: Optional[str] = None, icon: str = "📊"
) -> str:
    """
    Generate HTML for a metric card.

    Args:
        label: Metric label
        value: Metric value
        delta: Optional delta/change indicator
        icon: Emoji icon for the card

    Returns:
        HTML string for the metric card
    """
    delta_html = f'<div class="metric-delta">{delta}</div>' if delta else ""
    return f"""
    <div class="metric-card glass-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-content">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            {delta_html}
        </div>
    </div>
    """


def init_session_state() -> None:
    """Initialize all required session state variables."""
    defaults = {
        "current_page": "Home",
        "chat_history": [],
        # Startup validation form data
        "startup_idea": "",
        "industry": "",
        "country": "",
        "budget": 0,
        "keywords": [],
        # Backend response
        "backend_response": None,
        "report": None,
        "form_validated": False,
        "pipeline_status": "idle",
        "pipeline_progress": 0.0,
        "current_agent": "",
        "agent_timeline": [],
        "settings": {
            "theme": "dark",
            "animations": True,
            "auto_refresh": False,
        },
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
