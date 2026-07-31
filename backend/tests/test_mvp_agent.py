import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.mvp_recommendation_agent import MvpRecommendationAgent


def main():

    idea = input("Enter startup idea: ")

    competitors = """
    Major competitors:
    RedBus
    AbhiBus
    MakeMyTrip
    """

    market_analysis = """
    Industry:
    Online Bus Booking

    Target Customers:
    Daily commuters
    Students
    Long-distance travelers

    Trends:
    Mobile booking
    Digital payments
    Real-time tracking

    Opportunities:
    Regional routes
    Operator partnerships

    Challenges:
    High competition
    Customer acquisition
    """

    swot_analysis = """
    Strengths:
    Convenient digital booking

    Weaknesses:
    New platform

    Opportunities:
    Underserved regional routes

    Threats:
    Established competitors

    Risks:
    Customer acquisition
    """

    print("\nMVP TEST START")
    print("Calling MVP model...")

    agent = MvpRecommendationAgent()

    result = agent.analyze(
        idea,
        competitors,
        market_analysis,
        swot_analysis
    )

    print("\nMVP TEST RESULT:")
    print(result)


if __name__ == "__main__":
    main()