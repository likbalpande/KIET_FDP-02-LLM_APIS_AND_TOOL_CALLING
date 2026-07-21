import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def chat_completion(messages):
    contents = [types.Content(role=msg["role"], parts=[types.Part(text=msg["content"])]) for msg in messages]

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite", # gemini-3-flash-preview, gemini-3.5-flash
        contents=contents,
        config=types.GenerateContentConfig(system_instruction="You are helpful assistant. Keep it short. Answer in hinglish. No extra formatting."),
    )

    return response.text