# This file was auto-generated by Fern from our API Definition.

from .types import (
    Accent,
    AddAgentSecretResponseModel,
    AddChapterResponseModel,
    AddKnowledgeBaseResponseModel,
    AddProjectResponseModel,
    AddPronunciationDictionaryResponseModel,
    AddPronunciationDictionaryRulesResponseModel,
    AddVoiceIvcResponseModel,
    AddVoiceResponseModel,
    Age,
    AgentBan,
    AgentConfig,
    AgentConfigOverride,
    AgentConfigOverrideConfig,
    AgentMetadataResponseModel,
    AgentPlatformSettings,
    AgentSummaryResponseModel,
    AllowlistItem,
    ArrayJsonSchemaProperty,
    ArrayJsonSchemaPropertyItems,
    AsrConversationalConfig,
    AsrInputFormat,
    AsrProvider,
    AsrQuality,
    AudioNativeCreateProjectResponseModel,
    AuthSettings,
    AuthorizationMethod,
    BanReasonType,
    BreakdownTypes,
    ChapterResponse,
    ChapterSnapshotResponse,
    ChapterSnapshotsResponse,
    ChapterState,
    ChapterStatisticsResponse,
    ClientEvent,
    ClientToolConfig,
    ConvAiNewSecretConfig,
    ConvAiSecretLocator,
    ConvAiStoredSecretConfig,
    ConversationChargingCommonModel,
    ConversationConfig,
    ConversationConfigClientOverride,
    ConversationConfigClientOverrideConfig,
    ConversationHistoryAnalysisCommonModel,
    ConversationHistoryEvaluationCriteriaResultCommonModel,
    ConversationHistoryFeedbackCommonModel,
    ConversationHistoryMetadataCommonModel,
    ConversationHistoryTranscriptCommonModel,
    ConversationHistoryTranscriptCommonModelRole,
    ConversationHistoryTranscriptToolCallCommonModel,
    ConversationHistoryTranscriptToolResultCommonModel,
    ConversationInitiationClientData,
    ConversationInitiationClientDataConfig,
    ConversationSignedUrlResponseModel,
    ConversationSummaryResponseModel,
    ConversationSummaryResponseModelStatus,
    ConversationTokenDbModel,
    ConversationTokenPurpose,
    ConversationalConfig,
    CreateAgentResponseModel,
    CreatePhoneNumberResponseModel,
    Currency,
    CustomLlm,
    DataCollectionResultCommonModel,
    DoDubbingResponse,
    DubbingMetadataResponse,
    EditProjectResponseModel,
    EmbedConfig,
    EmbedConfigAvatar,
    EmbedConfigAvatar_Image,
    EmbedConfigAvatar_Orb,
    EmbedConfigAvatar_Url,
    EmbedVariant,
    EvaluationSettings,
    EvaluationSuccessResult,
    ExtendedSubscriptionResponseModelBillingPeriod,
    ExtendedSubscriptionResponseModelCharacterRefreshPeriod,
    ExtendedSubscriptionResponseModelCurrency,
    FeedbackItem,
    FineTuningResponse,
    FineTuningResponseModelStateValue,
    Gender,
    GetAgentEmbedResponseModel,
    GetAgentLinkResponseModel,
    GetAgentResponseModel,
    GetAgentsPageResponseModel,
    GetChaptersResponse,
    GetConversationResponseModel,
    GetConversationResponseModelStatus,
    GetConversationsPageResponseModel,
    GetKnowledgeBaseReponseModel,
    GetKnowledgeBaseReponseModelType,
    GetLibraryVoicesResponse,
    GetPhoneNumberResponseModel,
    GetProjectsResponse,
    GetPronunciationDictionariesMetadataResponseModel,
    GetPronunciationDictionaryMetadataResponse,
    GetSpeechHistoryResponse,
    GetVoicesResponse,
    HistoryAlignmentResponseModel,
    HistoryAlignmentsResponseModel,
    HistoryItem,
    HttpValidationError,
    ImageAvatar,
    Invoice,
    KnowledgeBaseLocator,
    KnowledgeBaseLocatorType,
    LanguageResponse,
    LibraryVoiceResponse,
    LibraryVoiceResponseModelCategory,
    LiteralJsonSchemaProperty,
    LiteralJsonSchemaPropertyType,
    Llm,
    ManualVerificationFileResponse,
    ManualVerificationResponse,
    Model,
    ModelRatesResponseModel,
    ModelResponseModelConcurrencyGroup,
    ModerationStatusResponseModel,
    ModerationStatusResponseModelSafetyStatus,
    ModerationStatusResponseModelWarningStatus,
    ObjectJsonSchemaProperty,
    ObjectJsonSchemaPropertyPropertiesValue,
    OrbAvatar,
    OutputFormat,
    PhoneNumberAgentInfo,
    PostAgentAvatarResponseModel,
    PrivacyConfig,
    ProfilePageResponseModel,
    ProjectCreationMetaResponseModel,
    ProjectCreationMetaResponseModelStatus,
    ProjectCreationMetaResponseModelType,
    ProjectExtendedResponseModel,
    ProjectExtendedResponseModelAccessLevel,
    ProjectExtendedResponseModelApplyTextNormalization,
    ProjectExtendedResponseModelFiction,
    ProjectExtendedResponseModelQualityPreset,
    ProjectExtendedResponseModelTargetAudience,
    ProjectResponse,
    ProjectResponseModelAccessLevel,
    ProjectResponseModelFiction,
    ProjectResponseModelTargetAudience,
    ProjectSnapshotResponse,
    ProjectSnapshotUploadResponseModel,
    ProjectSnapshotUploadResponseModelStatus,
    ProjectSnapshotsResponse,
    ProjectState,
    PromptAgent,
    PromptAgentOverride,
    PromptAgentOverrideConfig,
    PromptAgentToolsItem,
    PromptAgentToolsItem_Client,
    PromptAgentToolsItem_Webhook,
    PromptEvaluationCriteria,
    PronunciationDictionaryAliasRuleRequestModel,
    PronunciationDictionaryPhonemeRuleRequestModel,
    PronunciationDictionaryVersionLocator,
    PronunciationDictionaryVersionResponseModel,
    PydanticPronunciationDictionaryVersionLocator,
    QueryParamsJsonSchema,
    ReaderResourceResponseModel,
    ReaderResourceResponseModelResourceType,
    RecordingResponse,
    RemovePronunciationDictionaryRulesResponseModel,
    ReviewStatus,
    Safety,
    SafetyEvaluation,
    SafetyRule,
    SpeechHistoryItemResponse,
    SpeechHistoryItemResponseModelSource,
    SpeechHistoryItemResponseModelVoiceCategory,
    Subscription,
    SubscriptionResponse,
    SubscriptionResponseModelBillingPeriod,
    SubscriptionResponseModelCharacterRefreshPeriod,
    SubscriptionResponseModelCurrency,
    SubscriptionStatus,
    TelephonyProvider,
    TextToSpeechAsStreamRequest,
    TtsConversationalConfig,
    TtsConversationalConfigOverride,
    TtsConversationalConfigOverrideConfig,
    TtsConversationalModel,
    TtsOptimizeStreamingLatency,
    TtsOutputFormat,
    TurnConfig,
    TurnMode,
    UrlAvatar,
    UsageCharactersResponseModel,
    User,
    UserFeedback,
    UserFeedbackScore,
    ValidationError,
    ValidationErrorLocItem,
    VerificationAttemptResponse,
    Voice,
    VoiceGenerationParameterOptionResponse,
    VoiceGenerationParameterResponse,
    VoicePreviewResponseModel,
    VoicePreviewsResponseModel,
    VoiceResponseModelCategory,
    VoiceResponseModelSafetyControl,
    VoiceSample,
    VoiceSettings,
    VoiceSharingModerationCheckResponseModel,
    VoiceSharingResponse,
    VoiceSharingResponseModelCategory,
    VoiceSharingState,
    VoiceVerificationResponse,
    WebhookToolApiSchemaConfig,
    WebhookToolApiSchemaConfigMethod,
    WebhookToolApiSchemaConfigRequestHeadersValue,
    WebhookToolConfig,
    WidgetFeedbackMode,
)
from .errors import UnprocessableEntityError
from . import (
    audio_isolation,
    audio_native,
    chapters,
    conversational_ai,
    dubbing,
    history,
    models,
    projects,
    pronunciation_dictionary,
    samples,
    speech_to_speech,
    text_to_sound_effects,
    text_to_speech,
    text_to_voice,
    usage,
    user,
    voice_generation,
    voices,
    workspace,
)
from .client import AsyncElevenLabs, ElevenLabs
from .conversational_ai import (
    BodyPatchesAnAgentSettingsV1ConvaiAgentsAgentIdPatchSecretsItem,
    BodyPatchesAnAgentSettingsV1ConvaiAgentsAgentIdPatchSecretsItem_New,
    BodyPatchesAnAgentSettingsV1ConvaiAgentsAgentIdPatchSecretsItem_Stored,
)
from .dubbing import DubbingGetTranscriptForDubRequestFormatType
from .environment import ElevenLabsEnvironment
from .history import HistoryGetAllRequestSource
from .play import play, save, stream
from .projects import ProjectsAddRequestFiction, ProjectsAddRequestTargetAudience
from .pronunciation_dictionary import (
    PronunciationDictionaryAddFromFileRequestWorkspaceAccess,
    PronunciationDictionaryRule,
    PronunciationDictionaryRule_Alias,
    PronunciationDictionaryRule_Phoneme,
)
from .text_to_speech import (
    BodyTextToSpeechStreamingV1TextToSpeechVoiceIdStreamPostApplyTextNormalization,
    BodyTextToSpeechStreamingWithTimestampsV1TextToSpeechVoiceIdStreamWithTimestampsPostApplyTextNormalization,
    BodyTextToSpeechV1TextToSpeechVoiceIdPostApplyTextNormalization,
    BodyTextToSpeechWithTimestampsV1TextToSpeechVoiceIdWithTimestampsPostApplyTextNormalization,
    TextToSpeechStreamWithTimestampsResponse,
    TextToSpeechStreamWithTimestampsResponseAlignment,
    TextToSpeechStreamWithTimestampsResponseNormalizedAlignment,
)
from .text_to_voice import TextToVoiceCreatePreviewsRequestOutputFormat
from .version import __version__
from .workspace import BodyUpdateMemberV1WorkspaceMembersPostWorkspaceRole

__all__ = [
    "Accent",
    "AddAgentSecretResponseModel",
    "AddChapterResponseModel",
    "AddKnowledgeBaseResponseModel",
    "AddProjectResponseModel",
    "AddPronunciationDictionaryResponseModel",
    "AddPronunciationDictionaryRulesResponseModel",
    "AddVoiceIvcResponseModel",
    "AddVoiceResponseModel",
    "Age",
    "AgentBan",
    "AgentConfig",
    "AgentConfigOverride",
    "AgentConfigOverrideConfig",
    "AgentMetadataResponseModel",
    "AgentPlatformSettings",
    "AgentSummaryResponseModel",
    "AllowlistItem",
    "ArrayJsonSchemaProperty",
    "ArrayJsonSchemaPropertyItems",
    "AsrConversationalConfig",
    "AsrInputFormat",
    "AsrProvider",
    "AsrQuality",
    "AsyncElevenLabs",
    "AudioNativeCreateProjectResponseModel",
    "AuthSettings",
    "AuthorizationMethod",
    "BanReasonType",
    "BodyPatchesAnAgentSettingsV1ConvaiAgentsAgentIdPatchSecretsItem",
    "BodyPatchesAnAgentSettingsV1ConvaiAgentsAgentIdPatchSecretsItem_New",
    "BodyPatchesAnAgentSettingsV1ConvaiAgentsAgentIdPatchSecretsItem_Stored",
    "BodyTextToSpeechStreamingV1TextToSpeechVoiceIdStreamPostApplyTextNormalization",
    "BodyTextToSpeechStreamingWithTimestampsV1TextToSpeechVoiceIdStreamWithTimestampsPostApplyTextNormalization",
    "BodyTextToSpeechV1TextToSpeechVoiceIdPostApplyTextNormalization",
    "BodyTextToSpeechWithTimestampsV1TextToSpeechVoiceIdWithTimestampsPostApplyTextNormalization",
    "BodyUpdateMemberV1WorkspaceMembersPostWorkspaceRole",
    "BreakdownTypes",
    "ChapterResponse",
    "ChapterSnapshotResponse",
    "ChapterSnapshotsResponse",
    "ChapterState",
    "ChapterStatisticsResponse",
    "ClientEvent",
    "ClientToolConfig",
    "ConvAiNewSecretConfig",
    "ConvAiSecretLocator",
    "ConvAiStoredSecretConfig",
    "ConversationChargingCommonModel",
    "ConversationConfig",
    "ConversationConfigClientOverride",
    "ConversationConfigClientOverrideConfig",
    "ConversationHistoryAnalysisCommonModel",
    "ConversationHistoryEvaluationCriteriaResultCommonModel",
    "ConversationHistoryFeedbackCommonModel",
    "ConversationHistoryMetadataCommonModel",
    "ConversationHistoryTranscriptCommonModel",
    "ConversationHistoryTranscriptCommonModelRole",
    "ConversationHistoryTranscriptToolCallCommonModel",
    "ConversationHistoryTranscriptToolResultCommonModel",
    "ConversationInitiationClientData",
    "ConversationInitiationClientDataConfig",
    "ConversationSignedUrlResponseModel",
    "ConversationSummaryResponseModel",
    "ConversationSummaryResponseModelStatus",
    "ConversationTokenDbModel",
    "ConversationTokenPurpose",
    "ConversationalConfig",
    "CreateAgentResponseModel",
    "CreatePhoneNumberResponseModel",
    "Currency",
    "CustomLlm",
    "DataCollectionResultCommonModel",
    "DoDubbingResponse",
    "DubbingGetTranscriptForDubRequestFormatType",
    "DubbingMetadataResponse",
    "EditProjectResponseModel",
    "ElevenLabs",
    "ElevenLabsEnvironment",
    "EmbedConfig",
    "EmbedConfigAvatar",
    "EmbedConfigAvatar_Image",
    "EmbedConfigAvatar_Orb",
    "EmbedConfigAvatar_Url",
    "EmbedVariant",
    "EvaluationSettings",
    "EvaluationSuccessResult",
    "ExtendedSubscriptionResponseModelBillingPeriod",
    "ExtendedSubscriptionResponseModelCharacterRefreshPeriod",
    "ExtendedSubscriptionResponseModelCurrency",
    "FeedbackItem",
    "FineTuningResponse",
    "FineTuningResponseModelStateValue",
    "Gender",
    "GetAgentEmbedResponseModel",
    "GetAgentLinkResponseModel",
    "GetAgentResponseModel",
    "GetAgentsPageResponseModel",
    "GetChaptersResponse",
    "GetConversationResponseModel",
    "GetConversationResponseModelStatus",
    "GetConversationsPageResponseModel",
    "GetKnowledgeBaseReponseModel",
    "GetKnowledgeBaseReponseModelType",
    "GetLibraryVoicesResponse",
    "GetPhoneNumberResponseModel",
    "GetProjectsResponse",
    "GetPronunciationDictionariesMetadataResponseModel",
    "GetPronunciationDictionaryMetadataResponse",
    "GetSpeechHistoryResponse",
    "GetVoicesResponse",
    "HistoryAlignmentResponseModel",
    "HistoryAlignmentsResponseModel",
    "HistoryGetAllRequestSource",
    "HistoryItem",
    "HttpValidationError",
    "ImageAvatar",
    "Invoice",
    "KnowledgeBaseLocator",
    "KnowledgeBaseLocatorType",
    "LanguageResponse",
    "LibraryVoiceResponse",
    "LibraryVoiceResponseModelCategory",
    "LiteralJsonSchemaProperty",
    "LiteralJsonSchemaPropertyType",
    "Llm",
    "ManualVerificationFileResponse",
    "ManualVerificationResponse",
    "Model",
    "ModelRatesResponseModel",
    "ModelResponseModelConcurrencyGroup",
    "ModerationStatusResponseModel",
    "ModerationStatusResponseModelSafetyStatus",
    "ModerationStatusResponseModelWarningStatus",
    "ObjectJsonSchemaProperty",
    "ObjectJsonSchemaPropertyPropertiesValue",
    "OrbAvatar",
    "OutputFormat",
    "PhoneNumberAgentInfo",
    "PostAgentAvatarResponseModel",
    "PrivacyConfig",
    "ProfilePageResponseModel",
    "ProjectCreationMetaResponseModel",
    "ProjectCreationMetaResponseModelStatus",
    "ProjectCreationMetaResponseModelType",
    "ProjectExtendedResponseModel",
    "ProjectExtendedResponseModelAccessLevel",
    "ProjectExtendedResponseModelApplyTextNormalization",
    "ProjectExtendedResponseModelFiction",
    "ProjectExtendedResponseModelQualityPreset",
    "ProjectExtendedResponseModelTargetAudience",
    "ProjectResponse",
    "ProjectResponseModelAccessLevel",
    "ProjectResponseModelFiction",
    "ProjectResponseModelTargetAudience",
    "ProjectSnapshotResponse",
    "ProjectSnapshotUploadResponseModel",
    "ProjectSnapshotUploadResponseModelStatus",
    "ProjectSnapshotsResponse",
    "ProjectState",
    "ProjectsAddRequestFiction",
    "ProjectsAddRequestTargetAudience",
    "PromptAgent",
    "PromptAgentOverride",
    "PromptAgentOverrideConfig",
    "PromptAgentToolsItem",
    "PromptAgentToolsItem_Client",
    "PromptAgentToolsItem_Webhook",
    "PromptEvaluationCriteria",
    "PronunciationDictionaryAddFromFileRequestWorkspaceAccess",
    "PronunciationDictionaryAliasRuleRequestModel",
    "PronunciationDictionaryPhonemeRuleRequestModel",
    "PronunciationDictionaryRule",
    "PronunciationDictionaryRule_Alias",
    "PronunciationDictionaryRule_Phoneme",
    "PronunciationDictionaryVersionLocator",
    "PronunciationDictionaryVersionResponseModel",
    "PydanticPronunciationDictionaryVersionLocator",
    "QueryParamsJsonSchema",
    "ReaderResourceResponseModel",
    "ReaderResourceResponseModelResourceType",
    "RecordingResponse",
    "RemovePronunciationDictionaryRulesResponseModel",
    "ReviewStatus",
    "Safety",
    "SafetyEvaluation",
    "SafetyRule",
    "SpeechHistoryItemResponse",
    "SpeechHistoryItemResponseModelSource",
    "SpeechHistoryItemResponseModelVoiceCategory",
    "Subscription",
    "SubscriptionResponse",
    "SubscriptionResponseModelBillingPeriod",
    "SubscriptionResponseModelCharacterRefreshPeriod",
    "SubscriptionResponseModelCurrency",
    "SubscriptionStatus",
    "TelephonyProvider",
    "TextToSpeechAsStreamRequest",
    "TextToSpeechStreamWithTimestampsResponse",
    "TextToSpeechStreamWithTimestampsResponseAlignment",
    "TextToSpeechStreamWithTimestampsResponseNormalizedAlignment",
    "TextToVoiceCreatePreviewsRequestOutputFormat",
    "TtsConversationalConfig",
    "TtsConversationalConfigOverride",
    "TtsConversationalConfigOverrideConfig",
    "TtsConversationalModel",
    "TtsOptimizeStreamingLatency",
    "TtsOutputFormat",
    "TurnConfig",
    "TurnMode",
    "UnprocessableEntityError",
    "UrlAvatar",
    "UsageCharactersResponseModel",
    "User",
    "UserFeedback",
    "UserFeedbackScore",
    "ValidationError",
    "ValidationErrorLocItem",
    "VerificationAttemptResponse",
    "Voice",
    "VoiceGenerationParameterOptionResponse",
    "VoiceGenerationParameterResponse",
    "VoicePreviewResponseModel",
    "VoicePreviewsResponseModel",
    "VoiceResponseModelCategory",
    "VoiceResponseModelSafetyControl",
    "VoiceSample",
    "VoiceSettings",
    "VoiceSharingModerationCheckResponseModel",
    "VoiceSharingResponse",
    "VoiceSharingResponseModelCategory",
    "VoiceSharingState",
    "VoiceVerificationResponse",
    "WebhookToolApiSchemaConfig",
    "WebhookToolApiSchemaConfigMethod",
    "WebhookToolApiSchemaConfigRequestHeadersValue",
    "WebhookToolConfig",
    "WidgetFeedbackMode",
    "__version__",
    "audio_isolation",
    "audio_native",
    "chapters",
    "conversational_ai",
    "dubbing",
    "history",
    "models",
    "play",
    "projects",
    "pronunciation_dictionary",
    "samples",
    "save",
    "speech_to_speech",
    "stream",
    "text_to_sound_effects",
    "text_to_speech",
    "text_to_voice",
    "usage",
    "user",
    "voice_generation",
    "voices",
    "workspace",
]
