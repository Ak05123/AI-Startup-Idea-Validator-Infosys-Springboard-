import sys
from pathlib import Path

# ============================================================
# PATH SETUP
# ============================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

# ============================================================
# IMPORT
# ============================================================

from app.agent_factory import run_with_fallback
from agents.conversational_advisor import conversational_advisor


def ask_advisor(
    question: str,
    validation_context: dict,
    thread_id: str = "default",
    conversation_history: list = None,
):
    """
    Send a user question to the Conversational Advisor
    using the completed startup validation context.

    conversation_history: optional list of previous chat
    messages, e.g. [{"role": "user", "content": "..."}, ...]
    so the advisor can stay consistent with the conversation.
    """

    # --------------------------------------------------------
    # Build the previous-conversation transcript (if any)
    # --------------------------------------------------------

    history_block = ""

    if conversation_history:

        lines = []

        for message in conversation_history:

            role = message.get("role", "user")
            content = str(message.get("content", "")).strip()

            if not content:
                continue

            speaker = "USER" if role == "user" else "ADVISOR"
            lines.append(f"{speaker}: {content}")

        if lines:

            history_block = ""
            history_block += "PREVIOUS CONVERSATION\n"
            history_block += "====================\n\n"
            history_block += "\n\n".join(lines)
            history_block += "\n\n====================\n\n"

    prompt = f"""
COMPLETED STARTUP VALIDATION
============================

{validation_context}

============================

{history_block}USER QUESTION
=============

{question}

Answer the user's question using the validation
context provided above.

If previous conversation is provided above, stay
consistent with it and use it for context.

Do not rerun the startup validation pipeline.

Do not invent competitors, statistics, or facts.

If the required information is not available in
the validation context, clearly say that it is
not available.
"""

    result = run_with_fallback(
        conversational_advisor,
        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        require_json=False
    )

    return result