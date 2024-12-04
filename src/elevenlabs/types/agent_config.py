# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
from .array_json_schema_property import ArrayJsonSchemaProperty
from .object_json_schema_property import ObjectJsonSchemaProperty
import typing
from .prompt_agent import PromptAgent
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class AgentConfig(UncheckedBaseModel):
    prompt: typing.Optional[PromptAgent] = None
    first_message: typing.Optional[str] = None
    language: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ArrayJsonSchemaProperty, AgentConfig=AgentConfig)
update_forward_refs(ObjectJsonSchemaProperty, AgentConfig=AgentConfig)