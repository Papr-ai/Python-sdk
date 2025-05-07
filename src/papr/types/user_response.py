# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserResponse"]


class UserResponse(BaseModel):
    user_id: str

    created_at: Optional[str] = None

    email: Optional[str] = None

    external_id: Optional[str] = None

    metadata: Optional[object] = None

    updated_at: Optional[str] = None
