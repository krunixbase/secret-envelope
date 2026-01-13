
from dataclasses import dataclass
from typing import Any, Dict

from .exceptions import InvalidEnvelopeError, UnsupportedVersionError


SUPPORTED_VERSIONS = {"1.0"}


@dataclass(frozen=True)
class Envelope:
    """
    Immutable representation of a secret-share envelope.
    """

    version: str
    share_id: str
    threshold: int
    payload: Any
    metadata: Dict[str, Any]

    def __post_init__(self) -> None:
        if self.version not in SUPPORTED_VERSIONS:
            raise UnsupportedVersionError(
                f"Unsupported envelope version: {self.version}"
            )

        if not isinstance(self.share_id, str) or not self.share_id:
            raise InvalidEnvelopeError("share_id must be a non-empty string")

        if not isinstance(self.threshold, int) or self.threshold <= 0:
            raise InvalidEnvelopeError("threshold must be a positive integer")

        if not isinstance(self.metadata, dict):
            raise InvalidEnvelopeError("metadata must be a dictionary")
