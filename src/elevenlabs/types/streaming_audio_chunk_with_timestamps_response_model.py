# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import typing
from .character_alignment_response_model import CharacterAlignmentResponseModel
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class StreamingAudioChunkWithTimestampsResponseModel(UncheckedBaseModel):
    audio_base_64: typing_extensions.Annotated[str, FieldMetadata(alias="audio_base64")] = pydantic.Field()
    """
    Base64 encoded audio data
    """

    alignment: typing.Optional[CharacterAlignmentResponseModel] = pydantic.Field(default=None)
    """
    Timestamp information for each character in the original text
    """

    normalized_alignment: typing.Optional[CharacterAlignmentResponseModel] = pydantic.Field(default=None)
    """
    Timestamp information for each character in the normalized text
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
