import os

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

class GeminiClient:

    def __init__(self):

        genai.configure(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        # for model in genai.list_models():
        #  if "generateContent" in model.supported_generation_methods:
        #   print(model.name)

        self.model = genai.GenerativeModel(
            "gemini-2.0-flash-lite"
        )

    def generate(self, prompt):

        response = self.model.generate_content(prompt)

        return response.text