


import markdown2
import pdfkit
import os

def generate_report(company, summary, use_cases, resources, competitors, chatbot_ideas):
    markdown = f"""
# 📘 AI Strategy Report for **{company}**

---

## 📊 Industry Summary
{summary}

---

## 💡 Proposed AI/ML/GenAI Use Cases
{use_cases}

---

## 📂 Relevant Datasets and Tools
{resources}

---

## 🏁 Competitor AI Strategies
{competitors}

---

## 🤖 Chatbot Suggestions
{chatbot_ideas}

---

*Generated using a Multi-Agent System powered by Gemini AI*
"""

    # Save markdown
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(markdown)
    print("✅ report.md saved")

    # Convert markdown to HTML
    html = markdown2.markdown(markdown)

    # Set path to wkhtmltopdf executable
    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"  # Change this if needed
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # Generate PDF
    pdfkit.from_string(html, "report.pdf", configuration=config)
    print("✅ report.pdf generated")
