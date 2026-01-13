"""
Public interface for the secret-envelope package.
"""

from .format import Envelope
from .exceptions import EnvelopeError

__all__ = [
    "Envelope",
    "EnvelopeError",
]
