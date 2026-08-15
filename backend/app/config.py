import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# API KEYS
# ============================================================

GEMINI_API_KEY_1 = os.getenv("GEMINI_API_KEY_1")
GEMINI_API_KEY_2 = os.getenv("GEMINI_API_KEY_2")
GEMINI_API_KEY_3 = os.getenv("GEMINI_API_KEY_3")


if not GEMINI_API_KEY_1:
    raise ValueError("GEMINI_API_KEY_1 not found.")

if not GEMINI_API_KEY_2:
    raise ValueError("GEMINI_API_KEY_2 not found.")

if not GEMINI_API_KEY_3:
    raise ValueError("GEMINI_API_KEY_3 not found.")


# ============================================================
# MODEL 1
# ============================================================

gemini_model_1 = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=GEMINI_API_KEY_1,
    timeout=120,
    max_retries=2,
)


# ============================================================
# MODEL 2
# ============================================================

gemini_model_2 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=GEMINI_API_KEY_2,
    timeout=120,
    max_retries=2,
)


# ============================================================
# MODEL 3
# ============================================================

gemini_model_3 = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=GEMINI_API_KEY_3,
    timeout=120,
    max_retries=2,
)


# ============================================================
# FALLBACK MODEL LIST
# ============================================================

gemini_models = [
    gemini_model_1,
    gemini_model_2,
    gemini_model_3,
]