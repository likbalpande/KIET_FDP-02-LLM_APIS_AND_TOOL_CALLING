import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def _to_gemini_tools(tools):
    if not tools:
        return None

    function_declarations = [
        types.FunctionDeclaration(
            name=tool["function"]["name"],
            description=tool["function"].get("description"),
            parameters=tool["function"].get("parameters"),
        )
        for tool in tools
    ]

    return [types.Tool(function_declarations=function_declarations)]


def chat_completion_with_tools(messages, tools=None):
    contents = [
        msg if isinstance(msg, types.Content) else types.Content(role=msg["role"], parts=[types.Part(text=msg["content"])])
        for msg in messages
    ]

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",  # gemini-3-flash-preview, gemini-3.5-flash
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction="You are helpful assistant. Keep it short. Answer in hinglish. No extra formatting. Don't assume any parameters",
            tools=_to_gemini_tools(tools),
        ),
    )

    return response.candidates[0].content
