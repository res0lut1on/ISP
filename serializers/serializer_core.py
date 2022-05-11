import types
from inspect import getmodule
import sys
import importlib
import builtins
import __main__


def serialize(item) -> any:
    """Serialize item to 'dict[str, Any]'."""

    def serialize_elements(item) -> dict[str, any]:
        """Serialize elements of iterable type."""
        elements = {}
        for i, element in enumerate(item):
            elements[f"el{i}"] = serialize(element)
        return elements

    def serialize_pub_attribs(item) -> dict[str, any]:
        """Serialize public attributes of item."""
        elements = {}
        pub_attributes = list(
            filter(lambda item: not item.startswith('_'), dir(item)))
        for attr in pub_attributes:
            elements[attr] = serialize(item.__getattribute__(attr))
        return elements

    return None

