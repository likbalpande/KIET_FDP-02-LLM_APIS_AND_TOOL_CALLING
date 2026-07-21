import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_text(user_prompt):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite", # gemini-3-flash-preview, gemini-3.5-flash
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction="Keep it short. Answer in hinglish. No extra formatting.",
        ),
    )

    return response.text
