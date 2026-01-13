class EnvelopeError(Exception):
    """Base exception for all envelope-related errors."""
    pass


class InvalidEnvelopeError(EnvelopeError):
    """Raised when an envelope structure is invalid or malformed."""
    pass


class UnsupportedVersionError(EnvelopeError):
    """Raised when the envelope version is not supported."""
    pass

