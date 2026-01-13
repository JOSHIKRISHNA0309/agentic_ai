import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("GOOGLE_API_KEY"))

from textwrap import dedent

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.models.groq import Groq

# Initialize the research agent with advanced journalistic capabilities
agent = Agent(model=Groq(id="llama-3.3-70b-versatile",api_key=os.getenv('GROQ_API_KEY')), markdown=True)

# Get the response in a variable
# run: RunOutput = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")