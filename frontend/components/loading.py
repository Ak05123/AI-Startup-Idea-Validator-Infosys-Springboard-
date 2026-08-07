"""
Loading animation components for the AI Startup Idea Validator.
"""

import streamlit as st
import time
from typing import List, Optional, Callable

from utils.theme import SEARCH_STAGES


def render_agent_workflow(
    stages: List[str] = SEARCH_STAGES,
    on_progress: Optional[Callable] = None,
) -> None:
    """
    Render an animated AI agent workflow simulation.

    Args:
        stages: List of stage names to display
        on_progress: Optional callback with (stage_index, stage_name, progress)
    """
    import random

    # Container for the workflow
    st.markdown(
        """
        <div class="glass-card" style="margin: 1.5rem 0;">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
                <div class="loading-spinner" style="width: 20px; height: 20px; border-width: 2px;"></div>
                <span style="font-size: 1rem; font-weight: 600;">AI Agent Workflow</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Stage container
    stage_container = st.empty()

    for i, stage in enumerate(stages):
        progress = (i + 1) / len(stages)
        
        # Simulate processing time
        delay = random.uniform(0.3, 0.7)
        
        # Build the stage list HTML
        stages_html = ""
        for j, s in enumerate(stages):
            if j < i:
                # Completed stage
                stages_html += f"""
                <div class="agent-stage completed">
                    <div class="agent-stage-icon" style="background: rgba(0,212,170,0.2); color: #00d4aa;">✓</div>
                    <div class="agent-stage-label" style="color: rgba(255,255,255,0.6);">{s}</div>
                    <div class="agent-stage-time">Done</div>
                </div>
                """
            elif j == i:
                # Active stage
                stages_html += f"""
                <div class="agent-stage active">
                    <div class="agent-stage-icon" style="background: rgba(0,102,255,0.2); color: #0066ff;">
                        <div class="loading-spinner" style="width: 14px; height: 14px; border-width: 2px;"></div>
                    </div>
                    <div class="agent-stage-label" style="color: #ffffff;">{s}</div>
                    <div class="agent-stage-time">Processing...</div>
                </div>
                """
            else:
                # Pending stage
                stages_html += f"""
                <div class="agent-stage pending">
                    <div class="agent-stage-icon" style="background: rgba(255,255,255,0.05); color: rgba(255,255,255,0.3);">○</div>
                    <div class="agent-stage-label" style="color: rgba(255,255,255,0.3);">{s}</div>
                    <div class="agent-stage-time">Pending</div>
                </div>
                """
        
        # Progress bar
        bar_color = "#00d4aa" if progress == 1 else "#0066ff"
        
        stage_container.markdown(
            f"""
            <div style="margin: 0.5rem 0;">
                <div style="margin-bottom: 0.75rem;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 0.4rem; padding: 0 0.25rem;">
                        <span style="color: rgba(255,255,255,0.5);">Progress</span>
                        <span style="color: {bar_color}; font-weight: 600;">{int(progress * 100)}%</span>
                    </div>
                    <div style="height: 4px; background: rgba(255,255,255,0.05); border-radius: 2px; overflow: hidden;">
                        <div style="height: 100%; width: {progress * 100}%; background: linear-gradient(135deg, #0066ff, #00d4aa); border-radius: 2px; transition: width 0.3s ease;"></div>
                    </div>
                </div>
                <div style="background: rgba(255,255,255,0.02); border-radius: 12px; padding: 0.25rem;">
                    {stages_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        if on_progress:
            on_progress(i, stage, progress)
        
        time.sleep(delay)

    # Final state
    stage_container.markdown(
        f"""
        <div style="margin: 0.5rem 0;">
            <div style="margin-bottom: 0.75rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 0.4rem; padding: 0 0.25rem;">
                    <span style="color: rgba(255,255,255,0.5);">Progress</span>
                    <span style="color: #00d4aa; font-weight: 600;">100%</span>
                </div>
                <div style="height: 4px; background: rgba(255,255,255,0.05); border-radius: 2px; overflow: hidden;">
                    <div style="height: 100%; width: 100%; background: linear-gradient(135deg, #0066ff, #00d4aa); border-radius: 2px;"></div>
                </div>
            </div>
            <div style="background: rgba(255,255,255,0.02); border-radius: 12px; padding: 0.25rem;">
                {''.join(f'''
                <div class="agent-stage completed">
                    <div class="agent-stage-icon" style="background: rgba(0,212,170,0.2); color: #00d4aa;">✓</div>
                    <div class="agent-stage-label" style="color: rgba(255,255,255,0.6);">{s}</div>
                    <div class="agent-stage-time">Done</div>
                </div>
                ''' for s in stages)}
            </div>
            <div style="text-align: center; margin-top: 1rem; padding: 0.75rem; background: rgba(0,212,170,0.1); border-radius: 8px; border: 1px solid rgba(0,212,170,0.2);">
                <span style="color: #00d4aa; font-weight: 600;">✓ All stages completed successfully</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_spinner(message: str = "Processing...") -> None:
    """
    Render a custom animated spinner with message.

    Args:
        message: Message to display alongside the spinner
    """
    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 3rem;">
            <div class="loading-spinner" style="width: 40px; height: 40px; border-width: 3px;"></div>
            <div style="margin-top: 1rem; font-size: 0.9rem; color: rgba(255,255,255,0.6);">{message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_typing_indicator() -> None:
    """Render a typing animation indicator."""
    st.markdown(
        """
        <div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )