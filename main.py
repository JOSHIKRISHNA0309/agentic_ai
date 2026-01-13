import os
from dotenv import load_dotenv
from datetime import datetime

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools

# Load environment variables
load_dotenv()

# Check API key
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("❌ GROQ_API_KEY not found in .env file")

# Create the agent
agent = Agent(
    model=Groq(
        id="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
    ),
    tools=[
        DuckDuckGoTools(),
        Newspaper4kTools()
    ],
    markdown=True,
)


# -------------------------------
# Research Task
# -------------------------------

TOPIC = "Agentic AI in 2025"

PROMPT = f"""
You are an advanced AI research agent.

Your task:
1. Search the web for latest information about: {TOPIC}
2. Open and read at least 3 high quality articles
3. Extract key points
4. Write a well-structured research report with:
   - Title
   - Introduction
   - Key Trends (bulleted)
   - Use-cases
   - Challenges
   - Conclusion

Be factual and structured.
"""

print("🚀 Starting research...\n")

# Run agent
response = agent.run(PROMPT)

# Print result
print("\n" + "=" * 80)
print("📄 FINAL REPORT:\n")
print(response.content)

# -------------------------------
# Save to file
# -------------------------------

output_dir = "reports"
os.makedirs(output_dir, exist_ok=True)

filename = f"reports/agentic_ai_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.content)

print("\n" + "=" * 80)
print(f"✅ Report saved to: {filename}")
pip 