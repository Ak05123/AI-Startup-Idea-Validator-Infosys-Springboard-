"""
Charts Component - Reusable Plotly chart generators for data visualization.
"""

import plotly.graph_objects as go
import plotly.express as px
from typing import Any, Dict, List, Optional


def _get_dark_layout(title: str = "") -> Dict[str, Any]:
    """Get a consistent dark theme layout for Plotly charts."""
    return {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font": {"color": "rgba(255,255,255,0.7)", "family": "Inter, sans-serif"},
        "title": {
            "text": title,
            "font": {"color": "#ffffff", "size": 14},
            "x": 0.5,
            "xanchor": "center",
        },
        "margin": {"l": 40, "r": 20, "t": 40, "b": 40},
        "legend": {
            "font": {"color": "rgba(255,255,255,0.6)", "size": 10},
            "bgcolor": "rgba(0,0,0,0)",
        },
        "xaxis": {
            "gridcolor": "rgba(255,255,255,0.05)",
            "zerolinecolor": "rgba(255,255,255,0.1)",
            "tickfont": {"color": "rgba(255,255,255,0.5)", "size": 10},
        },
        "yaxis": {
            "gridcolor": "rgba(255,255,255,0.05)",
            "zerolinecolor": "rgba(255,255,255,0.1)",
            "tickfont": {"color": "rgba(255,255,255,0.5)", "size": 10},
        },
        "hoverlabel": {
            "bgcolor": "#1a1a3e",
            "font": {"color": "#ffffff", "size": 12},
            "bordercolor": "rgba(255,255,255,0.1)",
        },
    }


def create_market_size_chart(
    years: List[int],
    values: List[float],
    title: str = "Market Size ($B)",
) -> go.Figure:
    """Create a market size area chart."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode="lines+markers",
        name="Market Size",
        line=dict(color="#0066ff", width=3),
        fill="tozeroy",
        fillcolor="rgba(0,102,255,0.1)",
        marker=dict(size=8, color="#0066ff", line=dict(color="#4d94ff", width=2)),
    ))
    fig.update_layout(**_get_dark_layout(title))
    fig.update_layout(
        yaxis=dict(ticksuffix="B"),
        hovermode="x unified",
    )
    return fig


def create_growth_chart(
    years: List[int],
    values: List[float],
    title: str = "Growth Rate (%)",
) -> go.Figure:
    """Create a growth rate line chart."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode="lines+markers",
        name="Growth Rate",
        line=dict(color="#00d4aa", width=3),
        fill="tozeroy",
        fillcolor="rgba(0,212,170,0.1)",
        marker=dict(size=8, color="#00d4aa", line=dict(color="#00d4aa", width=2)),
    ))
    fig.update_layout(**_get_dark_layout(title))
    fig.update_layout(
        yaxis=dict(ticksuffix="%"),
        hovermode="x unified",
    )
    return fig


def create_market_segment_chart(segments: List[Dict[str, Any]]) -> go.Figure:
    """Create a market segment pie/donut chart."""
    labels = [s.get("name", "") for s in segments]
    values = [s.get("percentage", 0) for s in segments]
    colors = ["#0066ff", "#4d94ff", "#00d4aa", "#ffd93d", "#ff6b6b", "#00b4d8"]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(colors=colors[:len(labels)]),
        textinfo="label+percent",
        textfont=dict(color="#ffffff", size=11),
        hovertemplate="<b>%{label}</b><br>Share: %{percent}<br>Size: %{value}%<extra></extra>",
    )])
    fig.update_layout(**_get_dark_layout("Market Segments"))
    return fig


def create_revenue_projection_chart(revenue_data: Dict[str, Any]) -> go.Figure:
    """Create a revenue projection bar chart."""
    years = revenue_data.get("years", [])
    revenue = revenue_data.get("revenue", [])
    costs = revenue_data.get("costs", [])

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=years,
        y=revenue,
        name="Revenue",
        marker=dict(color="#0066ff", line=dict(color="#4d94ff", width=1)),
        hovertemplate="Year: %{x}<br>Revenue: $%{y:,.0f}<extra></extra>",
    ))
    if costs:
        fig.add_trace(go.Bar(
            x=years,
            y=costs,
            name="Costs",
            marker=dict(color="rgba(255,107,107,0.7)", line=dict(color="#ff6b6b", width=1)),
            hovertemplate="Year: %{x}<br>Costs: $%{y:,.0f}<extra></extra>",
        ))
    fig.update_layout(**_get_dark_layout("Revenue Projection"))
    fig.update_layout(
        barmode="group",
        yaxis=dict(ticksuffix="$"),
        hovermode="x unified",
    )
    return fig


def create_competitor_share_chart(competitors: List[Dict[str, Any]]) -> go.Figure:
    """Create a competitor market share chart."""
    names = [c.get("name", "") for c in competitors]
    shares = [c.get("market_share", 0) for c in competitors]
    colors = ["#0066ff", "#4d94ff", "#00d4aa", "#ffd93d", "#ff6b6b", "#00b4d8"]

    fig = go.Figure(data=[go.Pie(
        labels=names,
        values=shares,
        hole=0.3,
        marker=dict(colors=colors[:len(names)]),
        textinfo="label+percent",
        textfont=dict(color="#ffffff", size=11),
        hovertemplate="<b>%{label}</b><br>Market Share: %{percent}<extra></extra>",
    )])
    fig.update_layout(**_get_dark_layout("Market Share Distribution"))
    return fig


def create_comparison_radar_chart(
    categories: List[str],
    values: List[float],
    title: str = "Comparison",
) -> go.Figure:
    """Create a radar chart for multi-dimensional comparison."""
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        name=title,
        line=dict(color="#0066ff", width=2),
        fillcolor="rgba(0,102,255,0.2)",
    ))
    fig.update_layout(**_get_dark_layout(title))
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor="rgba(255,255,255,0.1)",
                tickfont=dict(color="rgba(255,255,255,0.5)", size=9),
            ),
            angularaxis=dict(
                gridcolor="rgba(255,255,255,0.1)",
                tickfont=dict(color="rgba(255,255,255,0.7)", size=10),
            ),
        ),
        showlegend=False,
    )
    return fig


def create_timeline_gantt(phases: List[Dict[str, Any]]) -> go.Figure:
    """Create a Gantt chart for development timeline."""
    fig = go.Figure()
    colors = ["#0066ff", "#4d94ff", "#00d4aa", "#ffd93d"]

    for i, phase in enumerate(phases):
        fig.add_trace(go.Bar(
            x=[phase.get("duration", 1)],
            y=[phase.get("name", f"Phase {i+1}")],
            orientation="h",
            name=phase.get("name", f"Phase {i+1}"),
            marker=dict(color=colors[i % len(colors)]),
            hovertemplate="<b>%{y}</b><br>Duration: %{x} weeks<extra></extra>",
            text=[phase.get("duration", "")],
            textposition="inside",
            textfont=dict(color="#ffffff", size=11),
        ))

    fig.update_layout(**_get_dark_layout("Development Timeline"))
    fig.update_layout(
        barmode="stack",
        xaxis=dict(title="Weeks", tickfont=dict(size=10)),
        yaxis=dict(title="", tickfont=dict(size=11)),
        showlegend=False,
        height=250,
        margin={"l": 120, "r": 20, "t": 30, "b": 40},
    )
    return fig