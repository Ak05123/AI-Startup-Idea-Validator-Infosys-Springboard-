import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)
from app.config import mistral_model

response = mistral_model.invoke("Say hello.")

print(response.content)