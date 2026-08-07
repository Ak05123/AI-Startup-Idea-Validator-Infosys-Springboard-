from orchestrator import startup_validator


def validate_startup(idea: str):

    return startup_validator.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": idea
                }
            ]
        }
    )


if __name__ == "__main__":

    startup_idea = input("Enter Startup Idea: ")

    result = validate_startup(startup_idea)

    print(result)