

from my_agents.industry_research_agent import IndustryResearchAgent
from my_agents.use_case_generator_agent import UseCaseGeneratorAgent
from my_agents.resource_collector_agent import ResourceCollectorAgent
from generate_report import generate_report

company = input("Enter a company or industry: ")

# Run pipeline
industry_agent = IndustryResearchAgent()
summary_result = industry_agent.run(company)

use_case_agent = UseCaseGeneratorAgent()
use_case_result = use_case_agent.run(summary_result["summary"])

resource_agent = ResourceCollectorAgent()
resource_result = resource_agent.run(use_case_result["use_cases"])

# Show results
print("\n--- Industry Summary ---")
print(summary_result["summary"])
print("\n--- Use Cases ---")
print(use_case_result["use_cases"])
print("\n--- Resources ---")
print(resource_result["resources"])

# Save final report
generate_report(
    company,
    summary_result["summary"],
    use_case_result["use_cases"],
    resource_result["resources"]
)
