import mimetypes
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

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

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",  # gemini-3-flash-preview, gemini-3.5-flash
        contents=types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
        config=types.GenerateContentConfig(
            system_instruction=prompt or DEFAULT_PROMPT,
            response_mime_type="application/json",
        ),
    )

    return response.text
