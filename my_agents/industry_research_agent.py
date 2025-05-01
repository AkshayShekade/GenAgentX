


import google.generativeai as genai
from utils.web_search import search_web
from utils.prompts import industry_research_prompt
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class IndustryResearchAgent:
    def __init__(self, model_name="models/gemini-2.0-flash"):
        self.model = genai.GenerativeModel(model_name)

    def run(self, company_name: str) -> dict:
        web_content = search_web(company_name + " company profile industry focus")
        prompt = industry_research_prompt(company_name, web_content)
        response = self.model.generate_content(prompt)
        return {"company": company_name, "summary": response.text.strip()}
