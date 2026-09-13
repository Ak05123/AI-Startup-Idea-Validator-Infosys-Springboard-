import sys
from pathlib import Path
import json

# ============================================================
# PATH SETUP
# ============================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

# ============================================================
# IMPORTS
# ============================================================

from deepagents import create_deep_agent
from app.config import gemini_models

# ============================================================
# EXTRACT RESPONSE
# ============================================================

def extract_response(result):
    """
    Extract the final text response from
    a Deep Agent result.
    """

    response = result["messages"][-1].content

    # --------------------------------------------------------
    # Deep Agents may return content as a list
    # --------------------------------------------------------

    if isinstance(response, list):

        if response and isinstance(
            response[0],
            dict
        ):

            return response[0].get(
                "text",
                ""
            )

        return str(response)

    return response


# ============================================================
# CLEAN JSON RESPONSE
# ============================================================

def clean_json_response(response):
    """
    Remove accidental markdown formatting
    and validate the JSON response.
    """

    if not response:

        raise ValueError(
            "Empty response received."
        )

    response = response.strip()

    # --------------------------------------------------------
    # Remove ```json ... ```
    # --------------------------------------------------------

    if response.startswith("```json"):

        response = response[
            len("```json"):
        ].strip()

        if response.endswith("```"):

            response = response[
                :-3
            ].strip()

    # --------------------------------------------------------
    # Remove ``` ... ```
    # --------------------------------------------------------

    elif response.startswith("```"):

        response = response[
            len("```"):
        ].strip()

        if response.endswith("```"):

            response = response[
                :-3
            ].strip()

    # --------------------------------------------------------
    # Validate JSON
    # --------------------------------------------------------

    json.loads(response)

    return response


# ============================================================
# CREATE SPECIALIST DEEP AGENT
# ============================================================

def create_specialist_agent(
    agent_definition,
    model
):
    """
    Create a Deep Agent specialist using
    the supplied agent definition and Gemini model.
    """

    return create_deep_agent(

        model=model,

        tools=agent_definition.get(
            "tools",
            []
        ),

        system_prompt=agent_definition[
            "system_prompt"
        ],
    )


# ============================================================
# FALLBACK EXECUTION
# ============================================================

def run_with_fallback(
    agent_definition,
    payload,
    require_json=True
):
    """
    Run a specialist Deep Agent using
    four Gemini models.

    Fallback order:

        MODEL 1
            ↓ failure
        MODEL 2
            ↓ failure
        MODEL 3
            ↓ failure
        MODEL 4
            ↓ failure
        FINAL ERROR

    Errors are printed temporarily for
    deployment debugging.

    If require_json=True, an invalid JSON
    response is treated as a failure and
    the next model is attempted.
    """

    agent_name = agent_definition.get(
        "name",
        "unknown_agent"
    )

    last_error = None

    # ========================================================
    # TRY ALL FOUR MODELS
    # ========================================================

    for model in gemini_models:

        try:

            # ------------------------------------------------
            # CREATE SPECIALIST DEEP AGENT
            # ------------------------------------------------

            agent = create_specialist_agent(
                agent_definition,
                model
            )

            # ------------------------------------------------
            # INVOKE DEEP AGENT
            # ------------------------------------------------

            result = agent.invoke(
                payload
            )

            # ------------------------------------------------
            # EXTRACT RESPONSE
            # ------------------------------------------------

            response = extract_response(
                result
            )

            # ------------------------------------------------
            # VALIDATE JSON
            # ------------------------------------------------

            if require_json:

                response = clean_json_response(
                    response
                )

            # ------------------------------------------------
            # SUCCESS
            # ------------------------------------------------

            return response

        except Exception as error:

            # ------------------------------------------------
            # STORE ERROR
            # ------------------------------------------------

            last_error = error

            # ------------------------------------------------
            # TEMPORARILY PRINT ACTUAL ERROR
            # ------------------------------------------------

            print(
                f"\n{agent_name} ERROR: "
                f"{type(error).__name__}: "
                f"{error}"
            )

            # ------------------------------------------------
            # TRY NEXT MODEL
            # ------------------------------------------------

            continue

    # ========================================================
    # ALL FOUR MODELS FAILED
    # ========================================================

    if last_error is not None:
        raise last_error

    raise RuntimeError(
        f"{agent_name} could not complete the request."
    )
