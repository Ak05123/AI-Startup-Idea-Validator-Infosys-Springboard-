from state.schema import StartupState


def create_state(startup_idea: str) -> StartupState:

    return StartupState(

        startup_idea=startup_idea,

        search_results="",

        competitor_analysis="",

        market_analysis="",

        swot_analysis="",

        mvp_recommendation="",

        gtm_strategy="",

        final_report=""

    )