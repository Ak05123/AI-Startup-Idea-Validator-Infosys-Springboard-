import os
from dotenv import load_dotenv
from google import genai


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()


# ============================================================
# GET API KEY
# ============================================================

api_key = os.getenv("GEMINI_API_KEY_1")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY_1 not found."
    )


# ============================================================
# CREATE GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=api_key
)


# ============================================================
# LIST AVAILABLE MODELS
# ============================================================

print("\n========================================")
print("AVAILABLE GEMINI MODELS")
print("========================================\n")


for model in client.models.list():

    print(model.name)