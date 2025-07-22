import click
from agents import set_tracing_disabled
import asyncio
from src.cli.controller import run


set_tracing_disabled(disabled=True)


@click.command
def invoke():
    """Invoke agent workflow."""
    asyncio.run(run(session_id="session_123"))


if __name__ == "__main__":
    invoke()
