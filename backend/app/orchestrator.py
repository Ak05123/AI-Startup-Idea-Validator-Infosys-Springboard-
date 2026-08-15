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

from app.agent_factory import run_with_fallback
from app.pdf_generator import generate_report_pdf

from agents.competitor import competitor_agent
from agents.market_analysis import market_agent
from agents.swot_risk import swot_agent
from agents.mvp import mvp_agent
from agents.gtm import gtm_agent
from agents.report import report_agent


# ============================================================
# RUN ONE AGENT
# ============================================================

def run_agent(
    agent,
    idea,
    instruction
):
    """
    Run one agent using the centralized fallback.

    API errors are hidden from the terminal.
    """

    try:

        result = run_with_fallback(

            agent,

            {
                "messages": [
                    {
                        "role": "user",
                        "content": f"""
Startup Idea:

{idea}

{instruction}

Return ONLY valid JSON.
Do not use markdown.
Do not add explanations.
"""
                    }
                ]
            },

            require_json=True
        )

        return json.loads(result)

    except Exception:

        return None


# ============================================================
# MAIN VALIDATION PIPELINE
# ============================================================

def run_startup_validation(idea):

    # ========================================================
    # SHARED STATE
    # ========================================================

    shared_state = {

        "startup_idea": idea,

        "competitor_analysis": None,
        "market_analysis": None,
        "swot_analysis": None,
        "mvp_analysis": None,
        "gtm_analysis": None,

        "final_report": None,

        "competitor_status": {
            "status": "pending"
        },

        "market_status": {
            "status": "pending"
        },

        "swot_status": {
            "status": "pending"
        },

        "mvp_status": {
            "status": "pending"
        },

        "gtm_status": {
            "status": "pending"
        },

        "report_status": {
            "status": "pending"
        },

        "pdf_status": {
            "status": "pending"
        },

        "pipeline_status": "running"
    }


    # ========================================================
    # 1. COMPETITOR
    # ========================================================

    print("\n[1/6] Competitor Analysis...")

    result = run_agent(
        competitor_agent,
        idea,
        "Perform competitor analysis."
    )

    if result is not None:

        shared_state["competitor_analysis"] = result

        shared_state["competitor_status"] = {
            "status": "completed"
        }

        print("      ✓ Completed")

    else:

        shared_state["competitor_status"] = {
            "status": "failed"
        }

        print("      ⚠ Unavailable")


    # ========================================================
    # 2. MARKET
    # ========================================================

    print("\n[2/6] Market Analysis...")

    result = run_agent(
        market_agent,
        idea,
        "Perform market analysis."
    )

    if result is not None:

        shared_state["market_analysis"] = result

        shared_state["market_status"] = {
            "status": "completed"
        }

        print("      ✓ Completed")

    else:

        shared_state["market_status"] = {
            "status": "failed"
        }

        print("      ⚠ Unavailable")


    # ========================================================
    # 3. SWOT
    # ========================================================

    print("\n[3/6] SWOT Analysis...")

    result = run_agent(
        swot_agent,
        idea,
        "Perform SWOT and risk analysis."
    )

    if result is not None:

        shared_state["swot_analysis"] = result

        shared_state["swot_status"] = {
            "status": "completed"
        }

        print("      ✓ Completed")

    else:

        shared_state["swot_status"] = {
            "status": "failed"
        }

        print("      ⚠ Unavailable")


    # ========================================================
    # 4. MVP
    # ========================================================

    print("\n[4/6] MVP Analysis...")

    result = run_agent(
        mvp_agent,
        idea,
        "Design a practical MVP using ONLY the startup idea."
    )

    if result is not None:

        shared_state["mvp_analysis"] = result

        shared_state["mvp_status"] = {
            "status": "completed"
        }

        print("      ✓ Completed")

    else:

        shared_state["mvp_status"] = {
            "status": "failed"
        }

        print("      ⚠ Unavailable")


    # ========================================================
    # 5. GTM
    # ========================================================

    print("\n[5/6] GTM Analysis...")

    result = run_agent(
        gtm_agent,
        idea,
        "Create a concise Go-To-Market strategy using ONLY the startup idea."
    )

    if result is not None:

        shared_state["gtm_analysis"] = result

        shared_state["gtm_status"] = {
            "status": "completed"
        }

        print("      ✓ Completed")

    else:

        shared_state["gtm_status"] = {
            "status": "failed"
        }

        print("      ⚠ Unavailable")


    # ========================================================
    # 6. REPORT AGENT
    # ========================================================

    print("\n[6/6] Final Startup Validation...")

    try:

        report_payload = {

            "messages": [

                {
                    "role": "user",

                    "content": f"""
Create the final startup validation report
using the following shared state.

SHARED STATE:

{json.dumps(shared_state, indent=2)}

Evaluate the startup using all available analyses.

Return ONLY valid JSON.
"""
                }

            ]
        }


        report_result = run_with_fallback(
            report_agent,
            report_payload,
            require_json=True
        )


        final_report = json.loads(
            report_result
        )


        shared_state["final_report"] = final_report

        shared_state["report_status"] = {
            "status": "completed"
        }

        print("      ✓ Completed")


    except Exception:

        shared_state["report_status"] = {
            "status": "failed"
        }

        print("      ⚠ Unavailable")


    # ========================================================
    # PDF GENERATION
    # ========================================================

    print("\n[PDF] Generating Validation Report...")

    try:

        # ----------------------------------------------------
        # Create filename from startup idea
        # ----------------------------------------------------

        safe_name = "".join(
            character
            if character.isalnum()
            else "_"
            for character in idea
        ).strip("_")


        if not safe_name:

            safe_name = "startup"


        pdf_filename = (
            f"{safe_name}_validation_report.pdf"
        )


        # ----------------------------------------------------
        # Save in project root
        # ----------------------------------------------------

        project_root = Path(
            __file__
        ).resolve().parents[2]


        pdf_path = (
            project_root
            / pdf_filename
        )


        # ----------------------------------------------------
        # Generate PDF using COMPLETE shared state
        # ----------------------------------------------------

        generated_pdf = generate_report_pdf(
            shared_state,
            str(pdf_path)
        )


        shared_state["pdf_status"] = {
            "status": "completed",
            "path": generated_pdf
        }


        print("      ✓ PDF Generated")


    except Exception:

        shared_state["pdf_status"] = {
            "status": "failed"
        }

        print("      ⚠ PDF generation failed")


    # ========================================================
    # PIPELINE STATUS
    # ========================================================

    statuses = [

        shared_state["competitor_status"]["status"],
        shared_state["market_status"]["status"],
        shared_state["swot_status"]["status"],
        shared_state["mvp_status"]["status"],
        shared_state["gtm_status"]["status"],
        shared_state["report_status"]["status"],
        shared_state["pdf_status"]["status"]
    ]


    if all(
        status == "completed"
        for status in statuses
    ):

        shared_state["pipeline_status"] = (
            "completed"
        )

    else:

        shared_state["pipeline_status"] = (
            "partial"
        )


    return shared_state


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("\n========================================")
    print("       AI STARTUP IDEA VALIDATOR")
    print("========================================")


    idea = input(
        "\nEnter Startup Idea: "
    ).strip()


    if not idea:

        print(
            "\nStartup idea cannot be empty."
        )

        sys.exit(1)


    shared_state = run_startup_validation(
        idea
    )


    # ========================================================
    # FINAL STATUS
    # ========================================================

    print("\n========================================")
    print("          VALIDATION COMPLETE")
    print("========================================")


    print(
        f"\nPipeline Status: "
        f"{shared_state['pipeline_status'].upper()}"
    )


    print("\nAgent Status:")

    print(
        "  Competitor : "
        + shared_state["competitor_status"]["status"]
    )

    print(
        "  Market     : "
        + shared_state["market_status"]["status"]
    )

    print(
        "  SWOT       : "
        + shared_state["swot_status"]["status"]
    )

    print(
        "  MVP        : "
        + shared_state["mvp_status"]["status"]
    )

    print(
        "  GTM        : "
        + shared_state["gtm_status"]["status"]
    )

    print(
        "  Report     : "
        + shared_state["report_status"]["status"]
    )

    print(
        "  PDF        : "
        + shared_state["pdf_status"]["status"]
    )


    # ========================================================
    # PDF LOCATION
    # ========================================================

    if (
        shared_state["pdf_status"]["status"]
        == "completed"
    ):

        print(
            "\nPDF:"
        )

        print(
            shared_state["pdf_status"]["path"]
        )


    # ========================================================
    # FINAL REPORT
    # ========================================================

    if shared_state["final_report"]:

        print("\n========================================")
        print("        FINAL VALIDATION REPORT")
        print("========================================")

        print(
            json.dumps(
                shared_state["final_report"],
                indent=4
            )
        )