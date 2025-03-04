# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .voice_sample import VoiceSample
from .voice_response_model_category import VoiceResponseModelCategory
from .fine_tuning_response import FineTuningResponse
from .voice_settings import VoiceSettings
from .voice_sharing_response import VoiceSharingResponse
from .verified_voice_language_response_model import VerifiedVoiceLanguageResponseModel
from .voice_response_model_safety_control import VoiceResponseModelSafetyControl
from .voice_verification_response import VoiceVerificationResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Voice(UncheckedBaseModel):
    voice_id: str
    name: typing.Optional[str] = None
    samples: typing.Optional[typing.List[VoiceSample]] = None
    category: typing.Optional[VoiceResponseModelCategory] = None
    fine_tuning: typing.Optional[FineTuningResponse] = None
    labels: typing.Optional[typing.Dict[str, str]] = None
    description: typing.Optional[str] = None
    preview_url: typing.Optional[str] = None
    available_for_tiers: typing.Optional[typing.List[str]] = None
    settings: typing.Optional[VoiceSettings] = None
    sharing: typing.Optional[VoiceSharingResponse] = None
    high_quality_base_model_ids: typing.Optional[typing.List[str]] = None
    verified_languages: typing.Optional[typing.List[VerifiedVoiceLanguageResponseModel]] = None
    safety_control: typing.Optional[VoiceResponseModelSafetyControl] = None
    voice_verification: typing.Optional[VoiceVerificationResponse] = None
    permission_on_resource: typing.Optional[str] = None
    is_owner: typing.Optional[bool] = None
    is_legacy: typing.Optional[bool] = None
    is_mixed: typing.Optional[bool] = None
    created_at_unix: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
