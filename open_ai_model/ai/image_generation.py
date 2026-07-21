import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def generate_image(prompt, output_path="generated_image.png"):
    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024",
        n=1,
    )

    image_bytes = base64.b64decode(response.data[0].b64_json)
    Path(output_path).write_bytes(image_bytes)

    return output_path
