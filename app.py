import streamlit as st
from my_agents.industry_research_agent import IndustryResearchAgent
from my_agents.use_case_generator_agent import UseCaseGeneratorAgent
from my_agents.resource_collector_agent import ResourceCollectorAgent
from my_agents.competitive_analysis_agent import CompetitiveAnalysisAgent
from my_agents.chatbot_suggestions_agent import ChatbotSuggestionAgent
from generate_report import generate_report




# Page Config
st.set_page_config(page_title="GenAgentX", page_icon="🤖", layout="wide")


# Custom CSS
st.markdown("""
    <style>
        .title {
            font-size:36px;
            font-weight:800;
            text-align:center;
            padding:10px;
            background: linear-gradient(90deg, #2a9d8f, #264653);
            color:white;
            border-radius: 12px;
        }
        .footer {
            font-size:14px;
            text-align:center;
            padding:10px;
            color: #888;
            margin-top: 60px;
        }
        .report-button {
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title Bar

st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h1 style="color: #1E88E5;">🤖 GenAgentX - AI Strategy Engine</h1>
    <p style="font-size: 1.2rem;">Generate AI strategies, use cases, and resources for any company or industry</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")


# ---------- Streamlit UI ----------
st.sidebar.markdown("### 🛠️ Tools")
st.sidebar.markdown("1. **Industry Research Agent**: Summarizes the industry.")
st.sidebar.markdown("2. **Word Cloud From Summary**: Creates wordcloud visualization from summary.")
st.sidebar.markdown("3. **Use Case Generator Agent**: Generates AI/ML use cases.")
st.sidebar.markdown("4. **Resource Collector Agent**: Finds datasets and tools.")
st.sidebar.markdown("5. **Competitive Analysis Agent**: Analyzes competitors' AI strategies.")
st.sidebar.markdown("6. **Chatbot Suggestion Agent**: Suggests chatbot ideas.")
st.sidebar.markdown("7. **Report Generator**: Creates a comprehensive report.")


st.sidebar.markdown("---")
st.sidebar.markdown("### 📜 About")
st.sidebar.markdown("This app uses a multi-agent system to generate AI strategies for any company or industry.")
st.sidebar.markdown("Built with Streamlit and Gemini AI.")
st.sidebar.markdown("### 📧 Contact")
st.sidebar.markdown("For inquiries, please contact: [Email](mailto:akshayshekade757@gmail.com)")
st.sidebar.markdown("### 🌐 GitHub")
st.sidebar.markdown("[GitHub Repository](https://github.com/AkshayShekade/GenAgentX)")

st.sidebar.markdown("### 📜 Disclaimer")
st.sidebar.markdown("This app is for educational purposes only. The generated strategies are not guaranteed to be accurate or effective.")
st.sidebar.markdown("---")

company = st.text_input("Enter a company or industry:")
st.markdown("###### Example: `Tesla Electric Vehicles`, `Healthcare AI`, `Finance Fraud Detection`")
st.markdown("###### Note: The more specific the input, the better the results!")


if st.button("🪄 Generate AI Strategy"):
    # 1. Industry Summary
    with st.spinner("🔍 Researching the industry..."):
        industry_agent = IndustryResearchAgent()
        industry = industry_agent.run(company)

    st.subheader("📊 Industry Summary")
    st.markdown(industry["summary"])

    # 2. Use Case Generator
    with st.spinner("💡 Generating AI/ML Use Cases..."):
        use_case_agent = UseCaseGeneratorAgent()
        use_cases = use_case_agent.run(industry["summary"])

    with st.expander("💡 Click to view AI/ML Use Cases"):
        st.markdown(use_cases["use_cases"])

    # 3. Resource Collector
    with st.spinner("📂 Searching for Datasets/Tools..."):
        resource_agent = ResourceCollectorAgent()
        resources = resource_agent.run(use_cases["use_cases"])

    with st.expander("📁 Click to view Resources & Datasets"):
        st.markdown(resources["resources"])

    # 4. Competitive Analysis
    with st.spinner("🏁 Analyzing Competitors..."):
        comp_agent = CompetitiveAnalysisAgent()
        competitors = comp_agent.run(company)

    with st.expander("🏁 Competitor AI Strategies"):
        st.markdown(competitors)

    # 5. Chatbot Suggestions
    with st.spinner("🤖 Suggesting Chatbot Ideas..."):
        chatbot_agent = ChatbotSuggestionAgent()
        chatbot_ideas = chatbot_agent.run(industry["summary"])

    with st.expander("🤖 Chatbot Suggestions"):
        st.markdown(chatbot_ideas)

    # 6. Generate Final Report
    with st.spinner("📝 Preparing report..."):
        generate_report(
            company=company,
            summary=industry["summary"],
            use_cases=use_cases["use_cases"],
            resources=resources["resources"],
            competitors=competitors,
            chatbot_ideas=chatbot_ideas
        )

    st.success("✅ Report generated successfully!")
    st.markdown("### 📄 Download Your Report:")
    st.markdown("The report includes the industry summary, use cases, resources, competitive analysis, and chatbot suggestions.")
    st.markdown("You can download the report in Markdown or PDF format.")

    with open("report.md", "r", encoding="utf-8") as f:
        st.download_button("📥 Download Markdown Report", f.read(), file_name="AI_Strategy_Report.md")

    with open("report.pdf", "rb") as f:
        st.download_button("📄 Download PDF Report", f.read(), file_name="AI_Strategy_Report.pdf")


# Footer
st.markdown("---")
st.markdown('<div class="footer">Made with ❤️ using Streamlit, Gemini, and a Multi-Agent System</div>', unsafe_allow_html=True)
st.markdown('<div class="footer">© 2025 Akshay Shekade. All rights reserved.</div>', unsafe_allow_html=True)
