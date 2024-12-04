# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .client_event import ClientEvent
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ConversationConfig(UncheckedBaseModel):
    max_duration_seconds: typing.Optional[int] = None
    client_events: typing.Optional[typing.List[ClientEvent]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow