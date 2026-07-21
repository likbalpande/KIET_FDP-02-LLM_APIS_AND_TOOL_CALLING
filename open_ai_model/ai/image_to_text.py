import base64
import mimetypes
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

DEFAULT_PROMPT = "Describe this image in detail."


def describe_image(image_path, prompt=None):
    image_bytes = Path(image_path).read_bytes()
    mime_type = mimetypes.guess_type(image_path)[0] or "image/jpeg"
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt or DEFAULT_PROMPT},
                    {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{image_base64}"}},
                ],
            }
        ],
    )

    return response.choices[0].message.content
