


import google.generativeai as genai
from dotenv import load_dotenv
import os
from utils.prompts import use_case_generation_prompt

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class UseCaseGeneratorAgent:
    def __init__(self, model_name="models/gemini-2.0-flash"):
        self.model = genai.GenerativeModel(model_name)

    def run(self, industry_summary: str) -> dict:
        prompt = use_case_generation_prompt(industry_summary)
        response = self.model.generate_content(prompt)
        return {"use_cases": response.text.strip()}
