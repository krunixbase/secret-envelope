from typing import Any, Mapping

from .format import Envelope
from .exceptions import InvalidEnvelopeError


def validate_envelope(data: Mapping[str, Any]) -> Envelope:
    """
    Validate raw envelope data and return an Envelope instance.

    This function performs structural validation and delegates
    semantic checks to the Envelope constructor.
    """
    if not isinstance(data, Mapping):
        raise InvalidEnvelopeError("Envelope data must be a mapping")

    try:
        return Envelope(
            version=data["version"],
            share_id=data["share_id"],
            threshold=data["threshold"],
            payload=data.get("payload"),
            metadata=data.get("metadata", {}),
        )
    except KeyError as exc:
        raise InvalidEnvelopeError(
            f"Missing required envelope field: {exc.args[0]}"
        ) from exc

