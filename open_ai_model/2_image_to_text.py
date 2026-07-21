import sys
from pathlib import Path
from ai.image_to_text import describe_image

image_path = './image_1.png'

prompt = "Generate a joke based on this image"

description = describe_image(image_path, prompt)

print(description)
