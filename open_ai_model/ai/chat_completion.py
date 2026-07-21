import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chat_completion(messages):
    response = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages=[
            {"role": "system", "content": "You are helpful assistant. Keep it short. Answer in hinglish. No extra formatting."},
        ] + messages,
    )

    return response.choices[0].message.content
