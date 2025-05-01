


import google.generativeai as genai
from dotenv import load_dotenv
import os
from utils.prompts import dataset_search_prompt

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class ResourceCollectorAgent:
    def __init__(self, model_name="models/gemini-2.0-flash"):
        self.model = genai.GenerativeModel(model_name)

    def run(self, use_case_text: str) -> dict:
        prompt = dataset_search_prompt(use_case_text)
        response = self.model.generate_content(prompt)
        return {"resources": response.text.strip()}
