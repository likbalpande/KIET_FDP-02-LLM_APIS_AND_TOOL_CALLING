import base64
import mimetypes
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SAMPLE_JSON = """{
  "complaint_title": "short title",
  "date_of_incident": "most accurate understanding of date of incident",
  "place_of_incident": "most accurate understanding of place of complaint",
  "short_summary": "one sentence summary of what the image shows",
  "key_points": ["short bullet point", "short bullet point"]
}"""

DEFAULT_PROMPT = f"""Read the text in this image and return a JSON summary of it.
Follow this exact structure, for example:
{SAMPLE_JSON}
"""


def summarize_image_to_json(image_path, prompt=None):
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
        response_format={"type": "json_object"},
    )

    return response.choices[0].message.content
