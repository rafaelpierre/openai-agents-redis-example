from agents import Agent
from agents.model_settings import ModelSettings
from src.model.openai import GPT_4O
from src.agent.intent.instructions import intent_instructions

intent_agent = Agent(
    name="Intent investigator agent",
    handoff_description="A helpful agent that maintains a dialogue with customers to understand if their objective is related to personal mortgages.",
    instructions=intent_instructions,
    model=GPT_4O,
    model_settings=ModelSettings(temperature=0.1, max_tokens=100),
)
