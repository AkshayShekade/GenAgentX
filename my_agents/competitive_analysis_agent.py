

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class CompetitiveAnalysisAgent:
    def __init__(self, model_name="models/gemini-2.0-flash"):
        self.model = genai.GenerativeModel(model_name)

    def run(self, company_name: str) -> str:
        prompt = f"""
You are a competitive strategy AI.

Identify major competitors of **{company_name}** and summarize how they are using AI/ML or GenAI in their business.

Format the response with:
- Competitor Name
- AI Initiatives
- Strategic Goals
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()
