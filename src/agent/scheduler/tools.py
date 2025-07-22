from agents import function_tool, RunContextWrapper
from src.agent.context import ConversationContext
from agents_redis.session import RedisSession


@function_tool(
    name_override="finish_conversation_tool",
    description_override="Finishes the conversation",
)
async def finish_conversation_tool(ctx: RunContextWrapper[ConversationContext]) -> None:
    print("Finishing the conversation...")
    # Finishes the conversation by setting the status to 'completed'
    ctx.context.status = "completed"


@function_tool(
    name_override="get_appointment_info_tool",
    description_override="Retrieves information about a scheduled appointment",
)
async def get_appointment_info_tool(
    ctx: RunContextWrapper[ConversationContext],
) -> None:
    print("Retrieving appointment information...")
    session = RedisSession(
        session_id="session_123",
        redis_url="redis://redis:6379",
    )

    items = await session.get_items()
    return items
