import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from app.orchestrator import Coordinator


if __name__ == "__main__":

    coordinator = Coordinator()

    idea = input("Enter startup idea: ")

    result = coordinator.analyze_startup(idea)

    print("\n==============================")
    print("COMPETITOR ANALYSIS")
    print("==============================")

    print(result["competitors"])

    print("\n==============================")
    print("MARKET ANALYSIS")
    print("==============================")

    print(result["market_analysis"])

    print("\n==============================")
    print("SWOT AND RISK ANALYSIS")
    print("==============================")

    print(result["swot_analysis"])