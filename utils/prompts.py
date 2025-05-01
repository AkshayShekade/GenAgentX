


def industry_research_prompt(company_name, web_content):
    return f"""
You are an Industry Analyst AI.

Based on the information below about {company_name}, summarize:
1. The industry/domain it operates in.
2. Its main products or services.
3. Key operational or strategic focus areas.

--- WEB CONTENT START ---
{web_content}
--- WEB CONTENT END ---
Respond in bullet points.
"""

def use_case_generation_prompt(industry_summary):
    return f"""
You are an expert AI strategist.

Based on the industry summary below, generate 5-7 AI/ML/GenAI use cases tailored to the company’s operations and goals.

--- SUMMARY START ---
{industry_summary}
--- SUMMARY END ---

Include:
- Title
- Problem solved
- Type of AI/ML/GenAI method

Respond in markdown bullet format.
"""

def dataset_search_prompt(use_cases_markdown):
    return f"""
You are a research assistant AI.

For each of the following use cases, suggest:
- An open dataset or tool from Kaggle, HuggingFace, or GitHub
- Provide clickable links
- Mention the platform

--- USE CASES START ---
{use_cases_markdown}
--- USE CASES END ---

Respond in markdown.
"""
