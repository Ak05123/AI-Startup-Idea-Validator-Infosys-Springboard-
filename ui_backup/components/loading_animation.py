"""
Loading Animation Component - Animated pipeline progress with agent timeline.
"""

import streamlit as st
from typing import List, Tuple, Optional
import time


AGENT_STAGES = [
    ("🌐", "Web Search Agent", "Searching the web for market data, competitors, and trends"),
    ("📈", "Market Analysis Agent", "Analyzing market size, growth, and segments"),
    ("🏆", "Competitor Agent", "Identifying and analyzing competitors"),
    ("⚠️", "SWOT Agent", "Evaluating strengths, weaknesses, opportunities, threats"),
    ("💡", "MVP Agent", "Recommending minimum viable product features"),
    ("📢", "GTM Strategy Agent", "Planning go-to-market strategy"),
    ("📄", "Report Agent", "Generating comprehensive validation report"),
]


def render_agent_timeline(
    current_stage: int = 0,
    completed_stages: Optional[List[int]] = None,
) -> None:
    """
    Render an animated agent processing timeline.

    Args:
        current_stage: Index of the currently active stage
        completed_stages: List of indices of completed stages
    """
    if completed_stages is None:
        completed_stages = list(range(current_stage))

    st.markdown(
        """
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
            border-radius:16px;padding:1.5rem;margin-bottom:1.5rem;">
            <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1rem;">
                <span style="font-size:1.25rem;">🤖</span>
                <span style="font-size:1rem;font-weight:700;">AI Agent Pipeline</span>
                <span style="font-size:0.8rem;color:rgba(255,255,255,0.4);">
                    Processing your startup idea
                </span>
            </div>
        """,
        unsafe_allow_html=True,
    )

    for i, (icon, label, desc) in enumerate(AGENT_STAGES):
        if i < len(completed_stages):
            # Completed stage
            st.markdown(
                f"""
                <div class="agent-stage completed">
                    <div class="agent-stage-icon" style="background:rgba(0,212,170,0.2);color:#00d4aa;">
                        ✓
                    </div>
                    <div>
                        <div class="agent-stage-label" style="color:#00d4aa;">{icon} {label}</div>
                        <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);">{desc}</div>
                    </div>
                    <div class="agent-stage-time">✅ Done</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif i == current_stage:
            # Active stage
            st.markdown(
                f"""
                <div class="agent-stage active">
                    <div class="agent-stage-icon" style="background:rgba(0,102,255,0.2);color:#0066ff;">
                        ⏳
                    </div>
                    <div>
                        <div class="agent-stage-label" style="color:#4d94ff;">{icon} {label}</div>
                        <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);">{desc}</div>
                    </div>
                    <div class="agent-stage-time" style="color:#4d94ff;">Processing...</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            # Pending stage
            st.markdown(
                f"""
                <div class="agent-stage pending">
                    <div class="agent-stage-icon" style="background:rgba(255,255,255,0.05);color:rgba(255,255,255,0.3);">
                        {i + 1}
                    </div>
                    <div>
                        <div class="agent-stage-label" style="color:rgba(255,255,255,0.3);">{icon} {label}</div>
                        <div style="font-size:0.75rem;color:rgba(255,255,255,0.2);">{desc}</div>
                    </div>
                    <div class="agent-stage-time" style="color:rgba(255,255,255,0.2);">Waiting</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('</div>', unsafe_allow_html=True)


def render_loading_cards() -> None:
    """
    Render animated loading cards for visual feedback.
    """
    st.markdown(
        """
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-bottom:1.5rem;">
            <div style="padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
                border-radius:12px;text-align:center;animation:pulse 2s ease-in-out infinite;">
                <div style="font-size:1.5rem;margin-bottom:0.5rem;">🔍</div>
                <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Gathering Data</div>
            </div>
            <div style="padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
                border-radius:12px;text-align:center;animation:pulse 2s ease-in-out infinite 0.3s;">
                <div style="font-size:1.5rem;margin-bottom:0.5rem;">🧠</div>
                <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Analyzing</div>
            </div>
            <div style="padding:1.25rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
                border-radius:12px;text-align:center;animation:pulse 2s ease-in-out infinite 0.6s;">
                <div style="font-size:1.5rem;margin-bottom:0.5rem;">📊</div>
                <div style="font-size:0.8rem;color:rgba(255,255,255,0.5);">Generating Report</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_pipeline_progress(
    progress: float,
    current_agent: str = "",
) -> None:
    """
    Render a progress bar with current agent info.

    Args:
        progress: Progress value between 0.0 and 1.0
        current_agent: Name of the currently running agent
    """
    st.markdown(
        f"""
        <div style="margin-bottom:0.5rem;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
                <span style="font-size:0.85rem;color:rgba(255,255,255,0.6);">
                    🤖 {current_agent or "Initializing..."}
                </span>
                <span style="font-size:0.85rem;color:#4d94ff;font-weight:600;">
                    {int(progress * 100)}%
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(progress)


def simulate_pipeline(
    status_placeholder,
    progress_bar,
    timeline_placeholder,
) -> None:
    """
    Simulate the full pipeline execution with animated stages.

    Args:
        status_placeholder: Streamlit placeholder for status text
        progress_bar: Streamlit progress bar object
        timeline_placeholder: Streamlit placeholder for timeline
    """
    for i, (icon, label, desc) in enumerate(AGENT_STAGES):
        progress = (i + 1) / len(AGENT_STAGES)

        # Update progress bar
        progress_bar.progress(progress)

        # Update status
        status_placeholder.markdown(
            f"""
            <div style="text-align:center;padding:1rem;background:rgba(0,102,255,0.05);
                border:1px solid rgba(0,102,255,0.15);border-radius:12px;margin:0.5rem 0;">
                <span style="font-size:1.5rem;">{icon}</span>
                <span style="font-weight:600;color:#4d94ff;">{label}</span>
                <span style="color:rgba(255,255,255,0.6);"> — {desc}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Update timeline
        timeline_placeholder.empty()
        with timeline_placeholder.container():
            render_agent_timeline(current_stage=i)

        # Simulate processing time
        time.sleep(0.5)

    # Mark complete
    progress_bar.progress(1.0)
    status_placeholder.success("✅ All agents completed! Results ready.")
    time.sleep(0.3)
    status_placeholder.empty()