from agents import Runner
import click
from openai.types.responses import ResponseTextDeltaEvent
from src.agent.intent import intent_agent
from agents import RunContextWrapper, AgentUpdatedStreamEvent
import json
from src.agent.context import ConversationContext
from src.agent.scheduler.scheduler_agent import scheduler_agent
from src.agent.intent.intent_agent import intent_agent
from agents_redis.session import RedisSession


def try_parse_context(ctx_payload: str):
    try:
        json_ctx = json.loads(ctx_payload)
        ctx = ConversationContext(**json_ctx)
        return ctx
    except Exception as e:
        return None


async def run(session_id: str):
    # Agent handoff setup

    session = RedisSession(
        session_id=session_id,
        redis_url="redis://redis:6379",
    )
    intent_agent.handoffs = [scheduler_agent]
    scheduler_agent.handoffs = [intent_agent]

    # Initial setup
    current_agent = intent_agent
    current_question = "Hi, how can I help you today?"
    require_input = True
    ctx: RunContextWrapper[ConversationContext] = RunContextWrapper(
        context=ConversationContext()
    )
    current_context = ctx.context
    is_complete = False

    # Main loop to run the agent interaction
    while not is_complete:
        if require_input:
            click.echo(f"\n{current_question}\n")
            agent_input = click.prompt("Answer")

        result = Runner.run_streamed(
            starting_agent=current_agent,
            input=agent_input,
            context=current_context,
            session=session,
        )

        is_complete = result.context_wrapper.context.status == "completed"

        current_question = "Answer"
        current_context = result.context_wrapper.context

        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                raw_delta = event.data.delta
                parsed_ctx = try_parse_context(event.data.delta)
                if parsed_ctx:
                    current_context = parsed_ctx
                    require_input = False
                else:
                    print(raw_delta, end="", flush=True)
            elif event.type == "agent_updated_stream_event" and isinstance(
                event, AgentUpdatedStreamEvent
            ):
                print(f"\nHanded off to agent: {event.new_agent.name}\n")
                current_agent = event.new_agent
            else:
                pass
