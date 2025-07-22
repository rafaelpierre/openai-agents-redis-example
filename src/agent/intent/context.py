from pydantic import BaseModel, model_validator, ValidationError
from typing import Literal
from typing_extensions import Self


class IntentContext(BaseModel):
    """Context for Intent Agent"""

    label: Literal["mortgage", "insurance", "other", "<unknown>"] = "<unknown>"
