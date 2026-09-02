"""
AI Advisor page for the AI Startup Validator.

Provides a chat-style interface for asking questions about the
validation results. The UI is ready for the existing backend
advisor endpoint when available.
"""

import streamlit as st

from components import ui


# ------------------------------------------------------------------
# Example questions
# ------------------------------------------------------------------
EXAMPLE_QUESTIONS = [
    "Is this idea worth pursuing?",
    "What are my biggest risks?",
    "What should I build first?",
    "Why is my validation score low?",
    "Who is my target customer?",
    "What is my biggest competitive weakness?",
]


RECOMMENDATION_PROMPT = (
    "Based on my completed startup validation results, give me a clear, "
    "practical recommendation: should I proceed with this startup idea, "
    "proceed with caution, or reconsider it? Explain why using the "
    "existing validation data, and list the most important next steps."
)


def _append_message(role: str, content: str) -> None:
    """Append one message to the persistent chat history."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    st.session_state.chat_history.append({"role": role, "content": content})


def _ask_backend(question: str) -> str:
    """
    Send a question to the existing advisor, including the current
    conversation history (excluding the question itself). Returns the
    advisor's answer text or an error message.
    """
    import api_client

    response = st.session_state.validation_response
    history = [
        m for m in st.session_state.get("chat_history", [])
        if m.get("content")
    ]

    try:
        data = api_client.ask_advisor(
            question,
            response,
            conversation_history=history,
        )
        return data.get("answer", "") or "The advisor returned an empty answer."
    except api_client.BackendError as exc:
        return f"⚠️ {exc}"
    except Exception as exc:
        return f"⚠️ Unexpected error while contacting the advisor: {exc}"


# ------------------------------------------------------------------
# Render
# ------------------------------------------------------------------
def render_advisor() -> None:
    """Render the AI Advisor page."""
    response = st.session_state.validation_response

    if not response:
        st.info("No validation results available yet. Please validate a startup idea first.")
        return

    st.markdown(
        """
        <div class="page-heading">🤖 AI Advisor</div>
        <div class="page-subtitle">
            Ask anything about your startup validation.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Show the startup idea
    idea = response.get("startup_idea", "") if isinstance(response, dict) else ""
    if idea:
        st.markdown(
            f"""
            <div class="idea-card">
                <div class="idea-label">Startup Idea</div>
                <div class="idea-text">"{idea}"</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Example questions (only before the conversation starts)
    chat_history = st.session_state.get("chat_history", [])
    if not chat_history:
        st.markdown("**Try asking:**")
        cols = st.columns(2)
        for i, question in enumerate(EXAMPLE_QUESTIONS):
            col = cols[i % 2]
            with col:
                if st.button(question, key=f"example_q_{i}", use_container_width=True):
                    st.session_state.pending_question = question
                    st.rerun()

    # Render the full conversation (persists across Streamlit reruns)
    for message in chat_history:
        if message.get("role") == "user":
            with st.chat_message("user"):
                st.markdown(message.get("content", ""))
        else:
            with st.chat_message("assistant"):
                st.markdown(message.get("content", ""))

    # Recommendation button — uses ONLY the existing validation results
    if st.button(
        "💡 Get Recommendation",
        type="secondary",
        use_container_width=True,
    ):
        st.session_state.pending_question = RECOMMENDATION_PROMPT
        st.rerun()

    # Chat input — previous conversation stays visible above it
    question = st.chat_input("Ask a question about your validation...")

    pending = st.session_state.pop("pending_question", None) or question
    if not pending or not pending.strip():
        return

    pending = pending.strip()

    # Add the user message, get the answer, add it — both appended to
    # session state so the full conversation survives Streamlit reruns.
    _append_message("user", pending)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = _ask_backend(pending)
    _append_message("assistant", answer)
    st.rerun()
