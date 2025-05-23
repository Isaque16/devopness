"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    List,
    Optional,
    TypedDict,
    Union,
)

from pydantic import Field, StrictStr

from .. import DevopnessBaseModel
from .hook_trigger_when_conditions_inner import (
    HookTriggerWhenConditionsInner,
    HookTriggerWhenConditionsInnerPlain,
)


class HookTriggerWhen(DevopnessBaseModel):
    """
    HookTriggerWhen

    Attributes:
        events (List[str], optional): List of events that will trigger an outgoing hook
        conditions (List[HookTriggerWhenConditionsInner], optional): Conditions that must be met to trigger the hook
    """

    events: Optional[List[StrictStr]] = Field(
        default=None, description="List of events that will trigger an outgoing hook"
    )
    conditions: Optional[List[HookTriggerWhenConditionsInner]] = Field(
        default=None, description="Conditions that must be met to trigger the hook"
    )


class HookTriggerWhenPlain(TypedDict, total=False):
    """
    Plain version of HookTriggerWhen.
    """

    events: Optional[List[str]]
    conditions: Optional[
        List[
            Union[
                HookTriggerWhenConditionsInner,
                HookTriggerWhenConditionsInnerPlain,
            ]
        ]
    ]
