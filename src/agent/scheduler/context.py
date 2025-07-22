from pydantic import BaseModel
from typing import List


class SchedulerContext(BaseModel):
    """Context for Scheduler Agent"""

    available_timeslots: List[str] = [
        "2023-10-01 10:00",
        "2023-10-01 11:00",
        "2023-10-01 14:00",
    ]
    selected_timeslot: str = ""
