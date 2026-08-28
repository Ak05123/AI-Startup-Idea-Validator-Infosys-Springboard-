import sys
from pathlib import Path
import time

# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

# ==================================================
# IMPORTS
# ==================================================

from app.orchestrator import deep_agent


# ==================================================
# LIMIT OUTPUT SIZE
# ==================================================

def limit(text, max_chars=500):

    if text is None:
        return ""

    text = str(text)

    if len(text) <= max_chars:
        return text

    return text[:max_chars]


# ==================================================
# INVOKE DEEP AGENT
# ==================================================

def invoke_agent(prompt):

    try:

        result = deep_agent.invoke(

            {
                "messages": [

                    {
                        "role": "user",
                        "content": prompt
                    }

                ]
            }

        )

        content = result["messages"][-1].content

        if isinstance(content, list):

            text = []

            for block in content:

                if isinstance(block, dict):

                    if "text" in block:

                        text.append(block["text"])

            content = "\n".join(text)

        return content

    except Exception as e:

        print("\nDeep Agent Error")
        print(e)

        return None


# ==================================================
# COMPLETE VALIDATION
# ==================================================

def full_validation(startup_idea):

    print("\nRunning Competitor Analysis...\n")

    competitor = invoke_agent(

        f"""
Startup Idea:

{startup_idea}

Perform ONLY competitor analysis.

Delegate to competitor_agent.

Return only competitor analysis.
"""

    )

    if competitor is None:

        return {

            "error": "Competitor Analysis Failed"

        }

    time.sleep(2)

    print("\nRunning Market Analysis...\n")

    market = invoke_agent(

        f"""
Startup Idea:

{startup_idea}

Perform ONLY market analysis.

Delegate to market_agent.

Return only market analysis.
"""

    )

    if market is None:

        return {

            "error": "Market Analysis Failed"

        }

    time.sleep(2)

    print("\nRunning SWOT Analysis...\n")

    swot = invoke_agent(

        f"""
Startup Idea:

{startup_idea}

Competitor Summary:

{limit(competitor)}

Market Summary:

{limit(market)}

Perform ONLY SWOT analysis.

Delegate to swot_agent.

Return only SWOT analysis.
"""

    )

    if swot is None:

        return {

            "error": "SWOT Analysis Failed"

        }

    time.sleep(2)
    print("\nRunning MVP Recommendation...\n")

    mvp = invoke_agent(

        f"""
Startup Idea:

{startup_idea}

SWOT Summary:

{limit(swot)}

Perform ONLY MVP recommendation.

Delegate to mvp_agent.

Return only MVP recommendation.
"""

    )

    if mvp is None:

        return {

            "error": "MVP Recommendation Failed"

        }

    time.sleep(2)


    # ==================================================
    # GTM
    # ==================================================

    print("\nRunning GTM Strategy...\n")

    gtm = invoke_agent(

        f"""
Startup Idea:

{startup_idea}

MVP Summary:

{limit(mvp)}

Perform ONLY GTM strategy.

Delegate to gtm_agent.

Return only GTM strategy.
"""

    )

    if gtm is None:

        return {

            "error": "GTM Strategy Failed"

        }

    time.sleep(2)


    # ==================================================
    # REPORT
    # ==================================================

    print("\nRunning Final Report...\n")

    report = invoke_agent(

        f"""
Startup Idea:

{startup_idea}

Competitor Summary:

{limit(competitor)}

Market Summary:

{limit(market)}

SWOT Summary:

{limit(swot)}

MVP Summary:

{limit(mvp)}

GTM Summary:

{limit(gtm)}

Generate ONLY the startup validation report.

Delegate to report_agent.

Return only the final report.
"""

    )

    if report is None:

        return {

            "error": "Report Generation Failed"

        }


    # ==================================================
    # RETURN
    # ==================================================

    return {

        "competitor": competitor,

        "market": market,

        "swot": swot,

        "mvp": mvp,

        "gtm": gtm,

        "report": report

    }