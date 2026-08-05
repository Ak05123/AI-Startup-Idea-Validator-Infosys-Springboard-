"""
Chart components using Plotly for the AI Startup Idea Validator.
"""

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from typing import Dict, Any, List, Optional

# Plotly template for dark theme
DARK_TEMPLATE = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="rgba(255,255,255,0.8)"),
        xaxis=dict(
            gridcolor="rgba(255,255,255,0.05)",
            zerolinecolor="rgba(255,255,255,0.1)",
            title_font=dict(size=12),
            tickfont=dict(size=11),
        ),
        yaxis=dict(
            gridcolor="rgba(255,255,255,0.05)",
            zerolinecolor="rgba(255,255,255,0.1)",
            title_font=dict(size=12),
            tickfont=dict(size=11),
        ),
        legend=dict(
            font=dict(size=11),
            bgcolor="rgba(0,0,0,0)",
            bordercolor="rgba(255,255,255,0.1)",
        ),
        hoverlabel=dict(
            bgcolor="#1a1a3e",
            font_size=12,
            font_family="Inter, sans-serif",
        ),
        margin=dict(l=20, r=20, t=30, b=20),
    ),
    data=dict(
        scatter=[go.Scatter(marker=dict(line=dict(width=0)))],
    ),
)


def create_market_size_chart(years: List[int], values: List[float], title: str = "Market Size ($B)") -> go.Figure:
    """Create a market size area chart."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode="lines+markers",
        name="Market Size",
        line=dict(color="#0066ff", width=3),
        fill="tozeroy",
        fillcolor="rgba(0, 102, 255, 0.15)",
        marker=dict(size=8, color="#0066ff", line=dict(width=2, color="white")),
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16)),
        template=DARK_TEMPLATE,
        hovermode="x unified",
        showlegend=False,
        xaxis=dict(dtick=1),
    )
    
    return fig


def create_growth_chart(years: List[int], values: List[float], title: str = "AI Adoption Rate (%)") -> go.Figure:
    """Create a growth/trend line chart."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode="lines+markers",
        name="Adoption Rate",
        line=dict(color="#00d4aa", width=3),
        fill="tozeroy",
        fillcolor="rgba(0, 212, 170, 0.15)",
        marker=dict(size=8, color="#00d4aa", line=dict(width=2, color="white")),
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16)),
        template=DARK_TEMPLATE,
        hovermode="x unified",
        showlegend=False,
        xaxis=dict(dtick=1),
    )
    
    return fig


def create_competitor_share_chart(competitors: List[Dict[str, Any]]) -> go.Figure:
    """Create a competitor market share pie chart."""
    names = [c.get("name", "Unknown") for c in competitors]
    shares = [c.get("market_share", 0) for c in competitors]
    colors = ["#0066ff", "#4d94ff", "#00d4aa", "#ffd93d", "#ff6b6b"]
    
    fig = go.Figure(data=[go.Pie(
        labels=names,
        values=shares,
        hole=0.4,
        marker=dict(colors=colors[:len(names)]),
        textinfo="label+percent",
        textfont=dict(size=12),
        hovertemplate="<b>%{label}</b><br>Market Share: %{percent}<br>",
    )])
    
    fig.update_layout(
        title=dict(text="Market Share Distribution", font=dict(size=16)),
        template=DARK_TEMPLATE,
        showlegend=False,
        annotations=[dict(
            text=f"{sum(shares)}%",
            x=0.5, y=0.5,
            font_size=20,
            showarrow=False,
        )],
    )
    
    return fig


def create_funding_chart(funding_data: List[Dict[str, Any]]) -> go.Figure:
    """Create a funding timeline bar chart."""
    companies = [f.get("company", "Unknown") for f in funding_data]
    amounts_raw = [float(f.get("amount", "$0M").replace("$", "").replace("M", "").replace("B", "")) * (1000 if "B" in f.get("amount", "") else 1) for f in funding_data]
    rounds = [f.get("round", "Round") for f in funding_data]
    
    colors = ["#0066ff", "#4d94ff", "#00d4aa", "#ffd93d"]
    
    fig = go.Figure(data=[go.Bar(
        x=companies,
        y=amounts_raw,
        marker=dict(
            color=colors[:len(companies)],
            line=dict(color="rgba(255,255,255,0.3)", width=1),
        ),
        text=[f.get("amount", "") for f in funding_data],
        textposition="outside",
        textfont=dict(size=11),
        hovertemplate="<b>%{x}</b><br>Amount: %{text}<br>Round: %{customdata}<br>",
        customdata=rounds,
    )])
    
    fig.update_layout(
        title=dict(text="Recent Funding Rounds", font=dict(size=16)),
        template=DARK_TEMPLATE,
        showlegend=False,
        yaxis=dict(title="Amount ($M)"),
        xaxis=dict(title=""),
    )
    
    return fig


def create_revenue_projection_chart(revenue_data: Dict[str, float]) -> go.Figure:
    """Create a revenue projection bar chart."""
    years = list(revenue_data.keys())
    values = list(revenue_data.values())
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=years,
        y=values,
        marker=dict(
            color=list(map(lambda v: "#0066ff" if v < 300 else "#00d4aa" if v < 500 else "#ffd93d", values)),
            line=dict(color="rgba(255,255,255,0.3)", width=1),
        ),
        text=[f"${v}K" for v in values],
        textposition="outside",
        textfont=dict(size=11),
        hovertemplate="<b>%{x}</b><br>Revenue: $%{y}K<br>",
    ))
    
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode="lines+markers",
        name="Trend",
        line=dict(color="#4d94ff", width=2, dash="dot"),
        marker=dict(size=6, color="#4d94ff"),
    ))
    
    fig.update_layout(
        title=dict(text="Revenue Projection ($K)", font=dict(size=16)),
        template=DARK_TEMPLATE,
        showlegend=False,
        yaxis=dict(title="Revenue ($K)"),
        xaxis=dict(title="", dtick=1),
    )
    
    return fig


def create_risk_heatmap(risks: List[Dict[str, Any]]) -> go.Figure:
    """Create a risk assessment scatter plot."""
    risk_names = [r.get("risk", "")[:30] + "..." for r in risks]
    probabilities = [r.get("probability", 0) * 100 for r in risks]
    impacts = [r.get("impact", 0) * 100 for r in risks]
    
    colors = ["#ff6b6b" if p > 60 and i > 60 else "#ffd93d" if p > 40 or i > 40 else "#00d4aa" for p, i in zip(probabilities, impacts)]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=probabilities,
        y=impacts,
        mode="markers+text",
        marker=dict(
            size=20,
            color=colors,
            line=dict(width=2, color="rgba(255,255,255,0.3)"),
        ),
        text=[r.get("risk", "")[:20] for r in risks],
        textposition="top center",
        textfont=dict(size=10, color="rgba(255,255,255,0.8)"),
        hovertemplate="<b>%{text}</b><br>Probability: %{x:.0f}%<br>Impact: %{y:.0f}%<br>",
    ))
    
    # Add quadrant lines
    fig.add_hline(y=50, line_dash="dash", line_color="rgba(255,255,255,0.2)")
    fig.add_vline(x=50, line_dash="dash", line_color="rgba(255,255,255,0.2)")
    
    fig.update_layout(
        title=dict(text="Risk Assessment Matrix", font=dict(size=16)),
        template=DARK_TEMPLATE,
        showlegend=False,
        xaxis=dict(title="Probability (%)", range=[0, 100]),
        yaxis=dict(title="Impact (%)", range=[0, 100]),
        shapes=[
            dict(
                type="rect",
                x0=0, y0=0, x1=50, y1=50,
                fillcolor="rgba(0, 212, 170, 0.05)",
                layer="below", line_width=0,
            ),
            dict(
                type="rect",
                x0=50, y0=50, x1=100, y1=100,
                fillcolor="rgba(255, 107, 107, 0.05)",
                layer="below", line_width=0,
            ),
        ],
    )
    
    return fig


def create_market_segment_chart(segments: List[Dict[str, Any]]) -> go.Figure:
    """Create a market segment treemap."""
    names = [s.get("name", "Unknown") for s in segments]
    sizes_raw = [float(s.get("size", "$0B").replace("$", "").replace("B", "").replace("M", "")) * (1 if "B" in s.get("size", "") else 0.001) for s in segments]
    growth_rates = [s.get("growth", "0%") for s in segments]
    
    fig = go.Figure(data=[go.Treemap(
        labels=names,
        parents=[""] * len(names),
        values=sizes_raw,
        textinfo="label+value+percent root",
        textfont=dict(size=14, color="white"),
        marker=dict(
            colors=["#0066ff", "#4d94ff", "#00d4aa", "#ffd93d"],
            line=dict(width=2, color="rgba(255,255,255,0.1)"),
        ),
        hovertemplate="<b>%{label}</b><br>Market Size: $%{value:.1f}B<br>Growth: %{customdata}<br>",
        customdata=growth_rates,
    )])
    
    fig.update_layout(
        title=dict(text="Market Segments", font=dict(size=16)),
        template=DARK_TEMPLATE,
        margin=dict(l=10, r=10, t=30, b=10),
    )
    
    return fig