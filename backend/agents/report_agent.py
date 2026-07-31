import sys
from pathlib import Path

# Add backend folder to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from app.config import model


class ReportAgent:

    def __init__(self):
        self.model = model

    def analyze(
        self,
        idea,
        competitors,
        market_analysis,
        swot_analysis,
        mvp_recommendation,
        gtm_strategy
    ):

        prompt = f"""
You are an AI Startup Validation Report and Scoring Agent.

Your job is NOT to repeat the previous analyses.

Your job is to evaluate the startup idea using the
results produced by the specialist agents and generate
a structured validation scorecard.

==================================================
STARTUP IDEA
==================================================

{idea}


==================================================
COMPETITOR ANALYSIS
==================================================

{competitors}


==================================================
MARKET ANALYSIS
==================================================

{market_analysis}


==================================================
SWOT AND RISK ANALYSIS
==================================================

{swot_analysis}


==================================================
MVP RECOMMENDATION
==================================================

{mvp_recommendation}


==================================================
GTM STRATEGY
==================================================

{gtm_strategy}


==================================================
SCORING FRAMEWORK
==================================================

Evaluate the startup using these categories.

1. Market Demand
Score: 0-100

Measure:
- evidence of customer demand
- size of target market
- growth potential
- customer need

2. Competitive Position
Score: 0-100

Measure:
- strength of competitors
- difficulty of entering the market
- competitive differentiation
- competitive advantage

IMPORTANT:
A HIGH competition level should reduce the score.

3. Problem Solution Fit
Score: 0-100

Measure:
- seriousness of customer problem
- usefulness of proposed solution
- alignment between problem and solution

4. MVP Feasibility
Score: 0-100

Measure:
- technical feasibility
- cost of building the MVP
- complexity
- ability to launch a focused first version

5. Differentiation
Score: 0-100

Measure:
- uniqueness of the startup
- defensibility
- differentiation from existing competitors

6. GTM Readiness
Score: 0-100

Measure:
- clarity of target customers
- acquisition channels
- positioning
- pricing
- launch strategy
- ability to acquire early users

7. Risk Management
Score: 0-100

Measure:
- number and severity of risks
- ability to mitigate those risks
- dependency on competitors, technology,
  regulation, operations or capital

IMPORTANT:
Higher risk should produce a LOWER score.

==================================================
OVERALL VALIDATION SCORE
==================================================

Calculate a weighted overall validation score.

Use this weighting:

Market Demand         = 20%
Competitive Position  = 15%
Problem Solution Fit  = 15%
MVP Feasibility       = 15%
Differentiation       = 15%
GTM Readiness         = 10%
Risk Management       = 10%

The final score must be between 0 and 100.

==================================================
VALIDATION CONFIDENCE
==================================================

Provide a "validation_confidence" score from 0 to 100.

This represents how strongly the available research
supports the assessment.

It is NOT statistical accuracy.

Higher confidence requires:
- stronger evidence
- more consistent information
- clearer market signals
- better-supported conclusions

==================================================
VIABILITY ESTIMATE
==================================================

Provide:

"viability_estimate_percent"

This is a MODEL-BASED ESTIMATE of startup viability,
not a guaranteed probability of success.

Use the overall score, evidence quality,
risks, competition and feasibility to estimate
the startup's current viability.

Do not claim that the percentage is a mathematically
proven probability of success.

==================================================
RISK LEVEL
==================================================

Classify the startup as exactly one of:

"Low"
"Medium"
"High"
"Very High"

Use the SWOT analysis and identified risks.

==================================================
FINAL VERDICT
==================================================

Choose exactly one:

"Strong Go"
"Go"
"Proceed with Caution"
"Needs Major Changes"
"Do Not Proceed"

Base this on the overall validation score,
risks, competition, MVP feasibility and market demand.

==================================================
RECOMMENDATION
==================================================

Provide the 3 most important actions the founder
should take next.

==================================================
RETURN FORMAT
==================================================

Return ONLY valid JSON.

Use exactly this structure:

{{
    "startup_idea": "",

    "scorecard": {{
        "market_demand": {{
            "score": 0,
            "reason": ""
        }},

        "competitive_position": {{
            "score": 0,
            "reason": ""
        }},

        "problem_solution_fit": {{
            "score": 0,
            "reason": ""
        }},

        "mvp_feasibility": {{
            "score": 0,
            "reason": ""
        }},

        "differentiation": {{
            "score": 0,
            "reason": ""
        }},

        "gtm_readiness": {{
            "score": 0,
            "reason": ""
        }},

        "risk_management": {{
            "score": 0,
            "reason": ""
        }}
    }},

    "overall_validation_score": 0,

    "validation_confidence": 0,

    "viability_estimate_percent": 0,

    "risk_level": "",

    "final_verdict": "",

    "strongest_factors": [],

    "weakest_factors": [],

    "key_risks": [],

    "next_actions": []
}}

==================================================
IMPORTANT RULES
==================================================

1. Return ONLY JSON.
2. Every score must be between 0 and 100.
3. Do not invent market facts.
4. Use the specialist-agent results as evidence.
5. Do not repeat the entire previous analyses.
6. Give concise reasons for every score.
7. Higher risk must reduce the Risk Management score.
8. Higher competition must reduce the Competitive Position score.
9. The overall validation score must follow the
   specified weighting.
10. validation_confidence is NOT statistical accuracy.
11. viability_estimate_percent is a model-based assessment,
    not a guaranteed probability of startup success.
12. Make the assessment practical and realistic.
"""

        try:

            response = self.model.invoke(prompt)

            return response.content

        except Exception as e:

            print("\n[Report Agent Error]")
            print(e)

            return "{}"