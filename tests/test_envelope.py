import pytest

from envelope.format import Envelope
from envelope.validate import validate_envelope
from envelope.exceptions import (
    EnvelopeError,
    InvalidEnvelopeError,
    UnsupportedVersionError,
)


def test_valid_envelope_creation():
    env = Envelope(
        version="1.0",
        share_id="share-001",
        threshold=3,
        payload=b"data",
        metadata={"owner": "test"},
    )

    assert env.version == "1.0"
    assert env.share_id == "share-001"
    assert env.threshold == 3
    assert env.payload == b"data"
    assert env.metadata["owner"] == "test"


def test_invalid_version_raises_error():
    with pytest.raises(UnsupportedVersionError):
        Envelope(
            version="2.0",
            share_id="share-001",
            threshold=3,
            payload=None,
            metadata={},
        )


def test_missing_required_field():
    data = {
        "version": "1.0",
        "threshold": 2,
        "payload": None,
        "metadata": {},
    }

    with pytest.raises(InvalidEnvelopeError):
        validate_envelope(data)


def test_invalid_threshold():
    with pytest.raises(InvalidEnvelopeError):
        Envelope(
            version="1.0",
            share_id="share-001",
            threshold=0,
            payload=None,
            metadata={},
        )


def test_validate_envelope_returns_instance():
    data = {
        "version": "1.0",
        "share_id": "share-xyz",
        "threshold": 5,
        "payload": "opaque",
        "metadata": {},
    }

    env = validate_envelope(data)
    assert isinstance(env, Envelope)


def test_non_mapping_input():
    with pytest.raises(EnvelopeError):
        validate_envelope("not-a-mapping")
