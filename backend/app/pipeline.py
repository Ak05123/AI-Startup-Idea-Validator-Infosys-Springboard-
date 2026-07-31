import sys
import time
from pathlib import Path

# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


# ==================================================
# IMPORT AGENTS
# ==================================================

from agents.web_search_agent import WebSearchAgent
from agents.competitor_agent import CompetitorAgent
from agents.market_analysis_agent import MarketAnalysisAgent
from agents.swot_risk_agent import SwotRiskAgent
from agents.mvp_recommendation_agent import MvpRecommendationAgent
from agents.gtm_strategy_agent import GtmStrategyAgent
from agents.report_agent import ReportAgent


# ==================================================
# STARTUP VALIDATION PIPELINE
# ==================================================

class StartupValidationPipeline:

    def __init__(self):

        self.web_agent = WebSearchAgent()
        self.competitor_agent = CompetitorAgent()
        self.market_agent = MarketAnalysisAgent()
        self.swot_agent = SwotRiskAgent()
        self.mvp_agent = MvpRecommendationAgent()
        self.gtm_agent = GtmStrategyAgent()
        self.report_agent = ReportAgent()


    # ==================================================
    # RESULT VALIDATION
    # ==================================================

    def _validate_result(self, result, step_name):

        if result is None:
            raise RuntimeError(
                f"{step_name} returned no result."
            )

        if isinstance(result, str):

            cleaned = result.strip()

            if not cleaned:
                raise RuntimeError(
                    f"{step_name} returned empty output."
                )

            if cleaned in {
                "{}",
                "[]",
                "None",
                "null"
            }:
                raise RuntimeError(
                    f"{step_name} returned empty data."
                )

        if isinstance(result, (list, tuple, dict)):

            if len(result) == 0:
                raise RuntimeError(
                    f"{step_name} returned empty data."
                )

        return result


    # ==================================================
    # RETRY HELPER
    # ==================================================

    def _run_with_retry(
        self,
        function,
        step_name,
        retries=3,
        delay=3
    ):

        last_error = None

        for attempt in range(1, retries + 1):

            try:

                print(
                    f"\n[{step_name}] "
                    f"Attempt {attempt}/{retries}"
                )

                result = function()

                result = self._validate_result(
                    result,
                    step_name
                )

                print(
                    f"[{step_name}] Success"
                )

                return result

            except Exception as error:

                last_error = error

                print(
                    f"\n[{step_name}] Failed:"
                )

                print(error)

                if attempt < retries:

                    wait_time = delay * attempt

                    print(
                        f"[{step_name}] "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)


        raise RuntimeError(
            f"{step_name} failed after "
            f"{retries} attempts: {last_error}"
        )


    # ==================================================
    # COMPETITOR
    # ==================================================

    def run_competitor(self, idea):

        print(
            "\n[Competitor] Starting..."
        )

        search_results = self._run_with_retry(

            lambda: self.web_agent.search(
                idea + " top competitors companies"
            ),

            "Competitor Search"
        )

        competitors = self._run_with_retry(

            lambda: self.competitor_agent.analyze(
                search_results
            ),

            "Competitor Analysis"
        )

        return competitors


    # ==================================================
    # MARKET
    # ==================================================

    def run_market(self, idea):

        print(
            "\n[Market] Starting..."
        )

        search_results = self._run_with_retry(

            lambda: self.web_agent.search(
                idea
                + " market size growth industry trends "
                + "target customers"
            ),

            "Market Search"
        )

        market_analysis = self._run_with_retry(

            lambda: self.market_agent.analyze(
                idea,
                search_results
            ),

            "Market Analysis"
        )

        return market_analysis


    # ==================================================
    # SWOT
    # ==================================================

    def run_swot(self, idea):

        print(
            "\n[SWOT] Starting..."
        )

        competitors = self.run_competitor(
            idea
        )

        market_analysis = self.run_market(
            idea
        )

        swot_analysis = self._run_with_retry(

            lambda: self.swot_agent.analyze(
                idea,
                competitors,
                market_analysis
            ),

            "SWOT Analysis"
        )

        return swot_analysis


    # ==================================================
    # MVP
    # ==================================================

    def run_mvp(self, idea):

        print(
            "\n[MVP] Starting..."
        )

        competitors = self.run_competitor(
            idea
        )

        market_analysis = self.run_market(
            idea
        )

        swot_analysis = self._run_with_retry(

            lambda: self.swot_agent.analyze(
                idea,
                competitors,
                market_analysis
            ),

            "SWOT Analysis"
        )

        mvp_recommendation = self._run_with_retry(

            lambda: self.mvp_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis
            ),

            "MVP Recommendation"
        )

        return mvp_recommendation


    # ==================================================
    # GTM
    # ==================================================

    def run_gtm(self, idea):

        print(
            "\n[GTM] Starting..."
        )

        competitors = self.run_competitor(
            idea
        )

        market_analysis = self.run_market(
            idea
        )

        swot_analysis = self._run_with_retry(

            lambda: self.swot_agent.analyze(
                idea,
                competitors,
                market_analysis
            ),

            "SWOT Analysis"
        )

        mvp_recommendation = self._run_with_retry(

            lambda: self.mvp_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis
            ),

            "MVP Recommendation"
        )

        gtm_strategy = self._run_with_retry(

            lambda: self.gtm_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis,
                mvp_recommendation
            ),

            "GTM Strategy"
        )

        return gtm_strategy


    # ==================================================
    # FINAL REPORT
    # ==================================================

    def run_report(self, idea):

        print(
            "\n[REPORT] Starting..."
        )

        competitors = self.run_competitor(
            idea
        )

        market_analysis = self.run_market(
            idea
        )

        swot_analysis = self._run_with_retry(

            lambda: self.swot_agent.analyze(
                idea,
                competitors,
                market_analysis
            ),

            "SWOT Analysis"
        )

        mvp_recommendation = self._run_with_retry(

            lambda: self.mvp_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis
            ),

            "MVP Recommendation"
        )

        gtm_strategy = self._run_with_retry(

            lambda: self.gtm_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis,
                mvp_recommendation
            ),

            "GTM Strategy"
        )

        report = self._run_with_retry(

            lambda: self.report_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis,
                mvp_recommendation,
                gtm_strategy
            ),

            "Final Report"
        )

        return report


    # ==================================================
    # TASK ROUTER
    # ==================================================

    def run_task(self, idea, task):

        task = task.strip().lower()

        # Accept a few common frontend/user names
        aliases = {
            "competitors": "competitor",
            "competition": "competitor",
            "market analysis": "market",
            "market_analysis": "market",
            "swot analysis": "swot",
            "swot_risk": "swot",
            "mvp recommendation": "mvp",
            "mvp_recommendation": "mvp",
            "gtm strategy": "gtm",
            "gtm_strategy": "gtm",
            "final report": "report",
            "final_report": "report",
            "validation report": "report",
            "complete": "full"
        }

        task = aliases.get(
            task,
            task
        )

        if task == "competitor":
            return self.run_competitor(idea)

        if task == "market":
            return self.run_market(idea)

        if task == "swot":
            return self.run_swot(idea)

        if task == "mvp":
            return self.run_mvp(idea)

        if task == "gtm":
            return self.run_gtm(idea)

        if task in {"report", "full"}:
            return self.run_report(idea)

        raise ValueError(
            "Invalid task. Use one of: "
            "competitor, market, swot, mvp, "
            "gtm, report, full"
        )


    # ==================================================
    # COMPLETE PIPELINE
    # ==================================================

    def run(self, idea):

        idea = idea.strip()

        if not idea:
            raise ValueError(
                "Startup idea cannot be empty."
            )

        competitors = self.run_competitor(
            idea
        )

        market_analysis = self.run_market(
            idea
        )

        swot_analysis = self._run_with_retry(

            lambda: self.swot_agent.analyze(
                idea,
                competitors,
                market_analysis
            ),

            "SWOT Analysis"
        )

        mvp_recommendation = self._run_with_retry(

            lambda: self.mvp_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis
            ),

            "MVP Recommendation"
        )

        gtm_strategy = self._run_with_retry(

            lambda: self.gtm_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis,
                mvp_recommendation
            ),

            "GTM Strategy"
        )

        report = self._run_with_retry(

            lambda: self.report_agent.analyze(
                idea,
                competitors,
                market_analysis,
                swot_analysis,
                mvp_recommendation,
                gtm_strategy
            ),

            "Final Report"
        )

        return {
            "startup_idea": idea,
            "competitors": competitors,
            "market_analysis": market_analysis,
            "swot_analysis": swot_analysis,
            "mvp_recommendation": mvp_recommendation,
            "gtm_strategy": gtm_strategy,
            "report": report
        }