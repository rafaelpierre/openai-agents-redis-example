from src.agent.intent.context import IntentContext
from agents import RunContextWrapper
import logging


async def on_intent_confirmation_handoff(ctx: RunContextWrapper[IntentContext]) -> None:
    logging.info(
        f"Handing off request from account number: {ctx.context.account_number}"
    )
