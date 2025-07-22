from pydantic import BaseModel
from src.agent.intent.context import IntentContext
from src.agent.scheduler.context import SchedulerContext
from typing import Literal


class ConversationContext(BaseModel):
    """Context for the conversation with the agent."""

    intent_context: IntentContext = IntentContext()
    scheduler_context: SchedulerContext = SchedulerContext()
    status: Literal["active", "completed"] = "active"
