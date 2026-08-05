import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from app.config import groq_model

response = groq_model.invoke("Say Hello")

print(response.content)