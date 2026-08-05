import sys
from pathlib import Path

# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)
from deepagents import create_deep_agent

from config import gemini_model_1

from tools.web_search import web_search

from agents.subagents.competitor import competitor_subagent
from agents.subagents.market_analysis import market_subagent
from agents.subagents.swot_risk import swot_subagent
from agents.subagents.mvp import mvp_subagent
from agents.subagents.gtm import gtm_subagent
from agents.subagents.report import report_subagent


startup_validator = create_deep_agent(
    model=gemini_model_1,

    tools=[
        web_search
    ],

    subagents=[
        competitor_subagent,
        market_subagent,
        swot_subagent,
        mvp_subagent,
        gtm_subagent,
        report_subagent,
    ],

    system_prompt="""
You are the Startup Validation Orchestrator.

You are responsible for coordinating specialist AI subagents.

Never perform specialist analysis yourself.

Delegate work to the appropriate subagent.

Available subagents:

• competitor_agent
    Research competitors and market gaps.

• market_analysis_agent
    Estimate TAM, SAM, SOM, demand and trends.

• swot_agent
    Perform SWOT analysis and identify risks.

• mvp_agent
    Recommend the minimum viable product.

• gtm_agent
    Create the Go-To-Market strategy.

• report_agent
    Generate the final startup validation report.

Always use the report_agent to produce the final response.

Do not invent information.

Always prefer tool-supported evidence.
"""
)