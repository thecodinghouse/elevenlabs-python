# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .review_task_instance_response_model import ReviewTaskInstanceResponseModel
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PaginatedListedReviewTaskInstanceModel(UncheckedBaseModel):
    review_tasks: typing.List[ReviewTaskInstanceResponseModel]
    cursor: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
