# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
from .array_json_schema_property import ArrayJsonSchemaProperty
from .object_json_schema_property import ObjectJsonSchemaProperty
import typing
from .llm import Llm
from .prompt_agent_tools_item import PromptAgentToolsItem
from .knowledge_base_locator import KnowledgeBaseLocator
from .custom_llm import CustomLlm
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class PromptAgent(UncheckedBaseModel):
    prompt: typing.Optional[str] = None
    llm: typing.Optional[Llm] = None
    temperature: typing.Optional[float] = None
    max_tokens: typing.Optional[int] = None
    tools: typing.Optional[typing.List[PromptAgentToolsItem]] = None
    knowledge_base: typing.Optional[typing.List[KnowledgeBaseLocator]] = None
    custom_llm: typing.Optional[CustomLlm] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ArrayJsonSchemaProperty, PromptAgent=PromptAgent)
update_forward_refs(ObjectJsonSchemaProperty, PromptAgent=PromptAgent)
