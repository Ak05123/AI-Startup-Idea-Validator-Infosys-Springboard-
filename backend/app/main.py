from orchestrator import Coordinator


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
