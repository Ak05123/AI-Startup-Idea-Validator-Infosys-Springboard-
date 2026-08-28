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

    # Example questions
    st.markdown("**Try asking:**")
    cols = st.columns(2)
    for i, question in enumerate(EXAMPLE_QUESTIONS):
        col = cols[i % 2]
        with col:
            if st.button(question, key=f"example_q_{i}", use_container_width=True):
                st.session_state.advisor_question = question
                st.rerun()

    st.markdown("---")

    # Chat input
    question = st.text_input(
        "Ask a question about your validation",
        value=st.session_state.get("advisor_question", ""),
        placeholder="e.g. What are my biggest risks?",
        key="advisor_input",
    )

    if st.button("Ask Advisor", type="primary", use_container_width=True):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            st.session_state.advisor_question = question.strip()
            try:
                import api_client
                data = api_client.ask_advisor(
                    question.strip(),
                    st.session_state.validation_response,
                )
                st.session_state.advisor_answer = data.get("answer", "")
                st.session_state.advisor_error = None
            except Exception as exc:
                st.session_state.advisor_answer = None
                st.session_state.advisor_error = str(exc)
            st.rerun()

    # Show errors from the last request
    advisor_error = st.session_state.get("advisor_error")
    if advisor_error:
        st.error(advisor_error)

    # Show answer if available
    answer = st.session_state.get("advisor_answer")
    if answer:
        st.markdown("### Answer")
        ui.render_card("AI Advisor", answer)
