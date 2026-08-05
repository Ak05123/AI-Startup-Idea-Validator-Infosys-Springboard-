import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from app.orchestrator import deep_agent

result = deep_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Say hello."
            }
        ]
    }
)

print(result["messages"][-1].content)