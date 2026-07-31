import sys
from pathlib import Path


# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


# ==================================================
# IMPORT
# ==================================================

from app.pipeline import StartupValidationPipeline


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    pipeline = StartupValidationPipeline()

    idea = input(
        "Enter startup idea: "
    ).strip()

    if not idea:

        print(
            "Startup idea cannot be empty."
        )

        sys.exit(1)


    # ==================================================
    # RUN COMPLETE PIPELINE
    # ==================================================

    try:

        result = pipeline.run(idea)


        # ==================================================
        # COMPETITOR
        # ==================================================

        print(
            "\n=============================="
        )

        print(
            "COMPETITOR ANALYSIS"
        )

        print(
            "=============================="
        )

        print(
            result["competitors"]
        )


        # ==================================================
        # MARKET
        # ==================================================

        print(
            "\n=============================="
        )

        print(
            "MARKET ANALYSIS"
        )

        print(
            "=============================="
        )

        print(
            result["market_analysis"]
        )


        # ==================================================
        # SWOT
        # ==================================================

        print(
            "\n=============================="
        )

        print(
            "SWOT AND RISK ANALYSIS"
        )

        print(
            "=============================="
        )

        print(
            result["swot_analysis"]
        )


        # ==================================================
        # MVP
        # ==================================================

        print(
            "\n=============================="
        )

        print(
            "MVP RECOMMENDATION"
        )

        print(
            "=============================="
        )

        print(
            result["mvp_recommendation"]
        )


        # ==================================================
        # GTM
        # ==================================================

        print(
            "\n=============================="
        )

        print(
            "GTM STRATEGY"
        )

        print(
            "=============================="
        )

        print(
            result["gtm_strategy"]
        )


        # ==================================================
        # FINAL REPORT
        # ==================================================

        print(
            "\n=============================="
        )

        print(
            "FINAL VALIDATION REPORT"
        )

        print(
            "=============================="
        )

        print(
            result["report"]
        )


    except Exception as error:

        print(
            "\n=============================="
        )

        print(
            "STARTUP VALIDATION ERROR"
        )

        print(
            "=============================="
        )

        print(
            error
        )