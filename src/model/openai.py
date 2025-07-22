from openai import AsyncAzureOpenAI
from agents import OpenAIChatCompletionsModel
import os

client = AsyncAzureOpenAI(
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
)

GPT_4O = OpenAIChatCompletionsModel(model="gpt-4o", openai_client=client)
