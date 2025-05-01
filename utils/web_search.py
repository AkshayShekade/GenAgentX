


from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")

def search_web(query, num_results=5):
    search = GoogleSearch({
        "q": query,
        "api_key": SERP_API_KEY,
        "num": num_results
    })
    results = search.get_dict().get("organic_results", [])
    content = ""
    for item in results:
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        content += f"{title}: {snippet}\n"
    return content
