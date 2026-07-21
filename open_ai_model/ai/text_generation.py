import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_text(user_prompt):
    response = client.responses.create(
        model="gpt-5.4-nano",
        instructions="Keep it short. Answer in hinglish. No extra formatting.",
        input=user_prompt,
    )

    return response.output_text
