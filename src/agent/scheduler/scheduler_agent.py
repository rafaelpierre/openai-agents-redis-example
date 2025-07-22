from agents import Agent
from agents.model_settings import ModelSettings
from src.model.openai import GPT_4O
from src.agent.scheduler.instructions import scheduler_instructions
from src.agent.scheduler.tools import (
    finish_conversation_tool,
    get_appointment_info_tool,
)

scheduler_agent = Agent(
    name="Appointment scheduler agent",
    handoff_description="A helpful agent that maintains a dialogue with customers to help them schedule an appointment, or retrieve info about previously scheduled appointments.",
    instructions=scheduler_instructions,
    model=GPT_4O,
    model_settings=ModelSettings(temperature=0.1, max_tokens=500),
    tools=[finish_conversation_tool, get_appointment_info_tool],
)
