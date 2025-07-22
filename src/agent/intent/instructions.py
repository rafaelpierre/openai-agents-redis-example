from agents import RunContextWrapper, Agent
from src.agent.context import ConversationContext
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from agents_redis.session import RedisSession


async def intent_instructions(
    ctx: RunContextWrapper[ConversationContext], agent: Agent[ConversationContext]
) -> str:
    instructions = (
        f"{RECOMMENDED_PROMPT_PREFIX}\n"
        f"You are an intent investigator agent. IntentContext stores the current conversation context and at the moment it looks like the following: {ctx.context.intent_context} \n"
        "Your task is to understand if the customer's objective is to get a personal mortgage, get his account number, and route them to SchedulerAgent if conditions are met.\n"
        "Follow the steps below. If any of the validation steps mentioned is not successful, don't move to the next step. \n"
        "2. Analyze the input from the customer. Based on the intention of the customer, update the IntentContext object with the appropriate value for the `label` attribute. \n"
        f"3. Customer intent label is `{ctx.context.intent_context.label}`. If the label is `mortgage`, hand over control to SchedulerAgent. If not, tell the customer that this service is only for mortgages and that you will not be able to assist them further.\n"
    )
    return instructions
