"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    List,
    Required,
    TypedDict,
    Union,
)

from pydantic import Field

from .. import DevopnessBaseModel
from .variable_targets import VariableTargets, VariableTargetsPlain


class ServerOptions(DevopnessBaseModel):
    """
    ServerOptions

    Attributes:
        variable_targets (List[VariableTargets]): The list of VariableTarget
    """

    variable_targets: List[VariableTargets] = Field(
        description="The list of VariableTarget"
    )


class ServerOptionsPlain(TypedDict, total=False):
    """
    Plain version of ServerOptions.
    """

    variable_targets: Required[
        List[
            Union[
                VariableTargets,
                VariableTargetsPlain,
            ]
        ]
    ]
