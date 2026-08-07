import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

keys = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
]

for i, key in enumerate(keys, start=1):
    print(f"\n========== KEY {i} ==========")

    try:
        client = genai.Client(api_key=key)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents="Say Hello"
        )

        print("SUCCESS")
        print(response.text)

    except Exception as e:
        print("FAILED")
        print(type(e).__name__)
        print(e)