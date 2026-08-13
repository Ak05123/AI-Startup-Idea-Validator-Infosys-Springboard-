import sys
from pathlib import Path

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

from app.config import gemini_model_2

from tools.web_search import web_search

from agents.competitor import competitor_agent
from agents.market_analysis import market_agent
from agents.swot_risk import swot_agent
from agents.mvp import mvp_agent
from agents.gtm import gtm_agent
from agents.report import report_agent


# ============================================================
# AGENT WRAPPERS
# ============================================================

def run_competitor_agent(startup_idea: str):
    """
    Run the Competitor Analysis Agent.
    """

    result = competitor_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Startup Idea:

{startup_idea}

Perform ONLY competitor analysis.

Return ONLY valid JSON.
"""
                }
            ]
        }
    )

    return result["messages"][-1].content


def run_market_agent(startup_idea: str):
    """
    Run the Market Analysis Agent.
    """

    result = market_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Startup Idea:

{startup_idea}

Perform ONLY market analysis.

Return ONLY valid JSON.
"""
                }
            ]
        }
    )

    return result["messages"][-1].content


def run_swot_agent(
    startup_idea: str,
    competitor_analysis: str,
    market_analysis: str
):
    """
    Run the SWOT Agent using previous analyses.
    """

    result = swot_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Startup Idea:

{startup_idea}

Competitor Analysis:

{competitor_analysis}

Market Analysis:

{market_analysis}

Perform ONLY SWOT analysis.

Use the supplied competitor and market analysis.

Return ONLY valid JSON.
"""
                }
            ]
        }
    )

    return result["messages"][-1].content


def run_mvp_agent(
    startup_idea: str,
    competitor_analysis: str,
    market_analysis: str,
    swot_analysis: str
):
    """
    Run the MVP Agent using previous analyses.
    """

    result = mvp_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Startup Idea:

{startup_idea}

Competitor Analysis:

{competitor_analysis}

Market Analysis:

{market_analysis}

SWOT Analysis:

{swot_analysis}

Design ONLY the Minimum Viable Product.

Use all supplied analysis.

Return ONLY valid JSON.
"""
                }
            ]
        }
    )

    return result["messages"][-1].content


def run_gtm_agent(
    startup_idea: str,
    competitor_analysis: str,
    market_analysis: str,
    swot_analysis: str,
    mvp_analysis: str
):
    """
    Run the GTM Agent using previous analyses.
    """

    result = gtm_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Startup Idea:

{startup_idea}

Competitor Analysis:

{competitor_analysis}

Market Analysis:

{market_analysis}

SWOT Analysis:

{swot_analysis}

MVP Plan:

{mvp_analysis}

Create ONLY the Go-To-Market strategy.

Use all supplied analysis.

Return ONLY valid JSON.
"""
                }
            ]
        }
    )

    return result["messages"][-1].content


def run_report_agent(
    startup_idea: str,
    competitor_analysis: str,
    market_analysis: str,
    swot_analysis: str,
    mvp_analysis: str,
    gtm_analysis: str
):
    """
    Run the Report Agent using all previous analyses.
    """

    result = report_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Generate the final Startup Validation Report.

Startup Idea:

{startup_idea}

Competitor Analysis:

{competitor_analysis}

Market Analysis:

{market_analysis}

SWOT Analysis:

{swot_analysis}

MVP Recommendation:

{mvp_analysis}

GTM Strategy:

{gtm_analysis}

Evaluate the startup using all supplied analyses.

Return ONLY valid JSON.
Do not explain.
Do not summarize.
Do not use markdown.
"""
                }
            ]
        }
    )

    return result["messages"][-1].content


# ============================================================
# STARTUP VALIDATION ORCHESTRATOR
# ============================================================

def validate_startup(startup_idea: str):

    # --------------------------------------------------------
    # STEP 1 — COMPETITOR ANALYSIS
    # --------------------------------------------------------

    competitor_analysis = run_competitor_agent(
        startup_idea
    )

    # --------------------------------------------------------
    # STEP 2 — MARKET ANALYSIS
    # --------------------------------------------------------

    market_analysis = run_market_agent(
        startup_idea
    )

    # --------------------------------------------------------
    # STEP 3 — SWOT ANALYSIS
    # --------------------------------------------------------

    swot_analysis = run_swot_agent(
        startup_idea,
        competitor_analysis,
        market_analysis

    )
    # --------------------------------------------------------
    # STEP 4 — MVP ANALYSIS
    # --------------------------------------------------------
    mvp_analysis = run_mvp_agent(
        startup_idea,
        competitor_analysis,
        market_analysis,
        swot_analysis 
    )

    # --------------------------------------------------------
    # STEP 5 — GTM ANALYSIS
    # --------------------------------------------------------

    gtm_analysis = run_gtm_agent(
        startup_idea,
        competitor_analysis,
        market_analysis,
        swot_analysis,
        mvp_analysis
    )

    # --------------------------------------------------------
    # STEP 6 — FINAL REPORT
    # --------------------------------------------------------

    final_report = run_report_agent(
        startup_idea,
        competitor_analysis,
        market_analysis,
        swot_analysis,
        mvp_analysis,
        gtm_analysis
    )

    # --------------------------------------------------------
    # RETURN COMPLETE RESULT
    # --------------------------------------------------------

    return {
        "startup_idea": startup_idea,
        "competitor_analysis": competitor_analysis,
        "market_analysis": market_analysis,
        "swot_analysis": swot_analysis,
        "mvp_analysis": mvp_analysis,
        "gtm_analysis": gtm_analysis,
        "final_report": final_report
    }


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    startup_idea = input(
        "Enter Startup Idea: "
    ).strip()

    result = validate_startup(
        startup_idea
    )

    print("\n========================================")
    print("      STARTUP VALIDATION RESULT")
    print("========================================")

    print("\nCOMPETITOR ANALYSIS:")
    print(result["competitor_analysis"])

    print("\nMARKET ANALYSIS:")
    print(result["market_analysis"])

    print("\nSWOT ANALYSIS:")
    print(result["swot_analysis"])

    print("\nMVP ANALYSIS:")
    print(result["mvp_analysis"])

    print("\nGTM STRATEGY:")
    print(result["gtm_analysis"])

    print("\nFINAL REPORT:")
    print(result["final_report"])

    print("\n========================================")