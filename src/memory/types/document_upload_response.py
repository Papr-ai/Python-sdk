# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentUploadResponse"]


class DocumentUploadResponse(BaseModel):
    progress: float
    """0.0 to 1.0 for percentage"""

    code: Optional[int] = None
    """HTTP status code"""

    current_filename: Optional[str] = None

    current_page: Optional[int] = None

    details: Optional[object] = None
    """Additional error details or context"""

    error: Optional[str] = None
    """Error message if failed"""

    message: Optional[str] = None
    """Human-readable status message"""

    status: Optional[str] = None
    """'success', 'processing', 'error', etc."""

    status_type: Optional[Literal["processing", "completed", "failed", "not_found", "queued", "cancelled"]] = None
    """Processing status type"""

    total_pages: Optional[int] = None

    upload_id: Optional[str] = None
