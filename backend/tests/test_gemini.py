import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from app.config import gemini_model

response = gemini_model.invoke("Say Hello")

print(response.content)