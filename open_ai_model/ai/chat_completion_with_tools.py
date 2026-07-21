import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def _to_message_dict(msg):
    if isinstance(msg, dict):
        return msg
    return msg.model_dump(exclude_none=True)


def chat_completion_with_tools(messages, tools=None):
    contents = [_to_message_dict(msg) for msg in messages]

    response = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages=[
            {
                "role": "system",
                "content": "You are helpful assistant. Keep it short. Answer in hinglish. No extra formatting. Don't assume any parameters",
            },
        ] + contents,
        tools=tools,
    )

    return response.choices[0].message
