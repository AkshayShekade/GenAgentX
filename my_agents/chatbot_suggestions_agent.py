

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class ChatbotSuggestionAgent:
    def __init__(self, model_name="models/gemini-2.0-flash"):
        self.model = genai.GenerativeModel(model_name)

    def run(self, summary: str) -> str:
        prompt = f"""
Suggest 2–3 AI-powered chatbot ideas for a company with the following profile:

--- START ---
{summary}
--- END ---

Explain:
- Chatbot Purpose (e.g., internal assistant, customer support)
- AI Capabilities
- Integration channel (e.g., WhatsApp, website, Slack)
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()
