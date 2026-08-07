"""
Chat UI Component - ChatGPT-like interface for the AI Advisor.
"""

import streamlit as st
from typing import List, Dict, Any, Optional
import time


def render_chat_message(
    role: str,
    content: str,
    avatar: str = "🤖",
) -> None:
    """
    Render a single chat message bubble.

    Args:
        role: 'user' or 'assistant'
        content: Message text content (may contain markdown)
        avatar: Emoji avatar for the message
    """
    if role == "assistant":
        st.markdown(
            f"""
            <div class="chat-message assistant">
                <div class="chat-avatar assistant">{avatar}</div>
                <div class="chat-bubble">{content}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="chat-message user">
                <div class="chat-avatar user">{avatar}</div>
                <div class="chat-bubble">{content}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_chat_history() -> None:
    """Render the full chat history from session state."""
    chat_history = st.session_state.get("chat_history", [])

    if not chat_history:
        # Show welcome message
        st.markdown(
            """
            <div style="text-align:center;padding:3rem 1rem;">
                <div style="font-size:3rem;margin-bottom:1rem;">🤖</div>
                <h3 style="font-size:1.25rem;font-weight:600;margin-bottom:0.5rem;">AI Startup Advisor</h3>
                <p style="font-size:0.9rem;color:rgba(255,255,255,0.5);max-width:500px;margin:0 auto;">
                    Ask me anything about your startup idea. I can help with market research,
                    competitor analysis, go-to-market strategy, and more.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    for message in chat_history:
        render_chat_message(
            role=message.get("role", "assistant"),
            content=message.get("content", ""),
            avatar=message.get("avatar", "🤖" if message.get("role") == "assistant" else "👤"),
        )


def render_suggested_questions(questions: List[str]) -> None:
    """
    Render suggested question buttons.

    Args:
        questions: List of suggested questions
    """
    if not questions:
        return

    st.markdown(
        """
        <div style="margin:1rem 0;">
            <div style="font-size:0.8rem;color:rgba(255,255,255,0.4);margin-bottom:0.5rem;">
                💡 Suggested questions:
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    for i, question in enumerate(questions):
        with cols[i % 2]:
            if st.button(
                question,
                key=f"suggested_q_{i}",
                use_container_width=True,
            ):
                st.session_state["pending_question"] = question
                st.rerun()


def render_chat_input() -> None:
    """
    Render the chat input area with send button.
    """
    st.markdown('<div style="margin-top:1rem;">', unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            "Ask the AI Advisor...",
            placeholder="Ask a question about your startup...",
            label_visibility="collapsed",
            key="chat_input_field",
            value=st.session_state.get("pending_question", ""),
        )
    with col2:
        send_clicked = st.button("Send", type="primary", use_container_width=True)

    if send_clicked or st.session_state.get("pending_question", ""):
        question = st.session_state.get("pending_question", "") or user_input
        if question.strip():
            # Add user message to chat
            chat_history = st.session_state.get("chat_history", [])
            chat_history.append({"role": "user", "content": question.strip(), "avatar": "👤"})
            st.session_state["chat_history"] = chat_history
            st.session_state["pending_question"] = ""
            st.session_state["process_question"] = True
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


def process_advisor_response() -> None:
    """
    Process a pending question by calling the backend advisor.
    This should be called before rendering to check if there's a question to process.
    """
    if not st.session_state.get("process_question", False):
        return

    chat_history = st.session_state.get("chat_history", [])
    if not chat_history:
        st.session_state["process_question"] = False
        return

    last_message = chat_history[-1]
    if last_message.get("role") != "user":
        st.session_state["process_question"] = False
        return

    question = last_message.get("content", "")

    # Show typing indicator
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Call backend advisor via API client
            from utils.api_client import ask_advisor

            form_data = {
                "startup_idea": st.session_state.get("startup_idea", ""),
                "industry": st.session_state.get("industry", ""),
                "country": st.session_state.get("country", ""),
                "keywords": st.session_state.get("keywords", []),
            }

            result = ask_advisor(question, form_data)

            if result["status"] == "success":
                response = result["response"]
            else:
                response = f"⚠️ {result['response']}"

            # Add assistant response to chat
            chat_history.append({"role": "assistant", "content": response, "avatar": "🤖"})
            st.session_state["chat_history"] = chat_history

    st.session_state["process_question"] = False
    st.rerun()


def render_advisor_page() -> None:
    """
    Render the complete AI Advisor page with chat UI.
    """
    # Process any pending question
    process_advisor_response()

    # Chat container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Render chat history
    chat_container = st.container()
    with chat_container:
        render_chat_history()

    # Suggested questions (only show when no history or last was assistant)
    chat_history = st.session_state.get("chat_history", [])
    if not chat_history or chat_history[-1].get("role") == "assistant":
        suggested = [
            "What's the market size for this idea?",
            "Who are my main competitors?",
            "What's a good MVP strategy?",
            "How should I price my product?",
            "What are the key risks?",
            "How do I acquire customers?",
        ]
        render_suggested_questions(suggested)

    # Chat input
    render_chat_input()

    st.markdown('</div>', unsafe_allow_html=True)