import os

from agno.agent import Agent
from agno.models.azure.ai_foundry import AzureAIFoundry
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()
azure_endpoint = os.getenv("AZURE_ENDPOINT")
api_key = os.getenv("AZURE_API_KEY")
api_version = os.getenv("AZURE_API_VERSION")


agent = Agent(
    model=AzureAIFoundry(
        id="DeepSeek-R1",
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version,
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
