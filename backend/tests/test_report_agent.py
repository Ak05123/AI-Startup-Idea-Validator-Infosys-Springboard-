import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from app.pipeline import StartupValidationPipeline
from agents.report_agent import ReportAgent


def main():

    idea = input(
        "Enter startup idea: "
    ).strip()

    print("\nREPORT TEST START")

    pipeline = StartupValidationPipeline()

    print("\nGenerating required analyses...")

    competitors = pipeline.run_competitor(
        idea
    )

    market_analysis = pipeline.run_market(
        idea
    )

    swot_analysis = pipeline.swot_agent.analyze(
        idea,
        competitors,
        market_analysis
    )

    mvp_recommendation = pipeline.mvp_agent.analyze(
        idea,
        competitors,
        market_analysis,
        swot_analysis
    )

    gtm_strategy = pipeline.gtm_agent.analyze(
        idea,
        competitors,
        market_analysis,
        swot_analysis,
        mvp_recommendation
    )

    report_agent = ReportAgent()

    result = report_agent.analyze(
        idea,
        competitors,
        market_analysis,
        swot_analysis,
        mvp_recommendation,
        gtm_strategy
    )

    print("\nFINAL REPORT RESULT:\n")
    print(result)


if __name__ == "__main__":
    main()