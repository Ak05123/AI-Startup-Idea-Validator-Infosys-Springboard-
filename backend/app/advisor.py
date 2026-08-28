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
    thread_id: str = "default"
):
    """
    Send a user question to the Conversational Advisor
    using the completed startup validation context.
    """

    prompt = f"""
COMPLETED STARTUP VALIDATION
============================

{validation_context}

============================

USER QUESTION
=============

{question}

Answer the user's question using the validation
context provided above.

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