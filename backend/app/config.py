import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found in the .env file."
    )


MODEL_NAME = "gemini-3.5-flash-lite"


model = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    api_key=GEMINI_API_KEY,
    timeout=120,
    max_retries=5
)