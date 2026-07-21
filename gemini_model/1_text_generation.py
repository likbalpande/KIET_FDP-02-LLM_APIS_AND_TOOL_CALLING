# pip install google-genai
# pip install dotenv

import sys
from pathlib import Path
from ai.text_generation import generate_text

user_prompt = "Explain what ai use in web app development is."

result = generate_text(user_prompt)
print(result)
