from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI


LLAMA_3_2 = OpenAIChatCompletionsModel(
    model="llama3.2",
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="FAKE_KEY"),
)
