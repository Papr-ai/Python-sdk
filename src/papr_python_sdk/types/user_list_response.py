# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .user_response import UserResponse

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    data: List[UserResponse]

    page: int

    page_size: int

    total: int
