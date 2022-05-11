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

    if isinstance(item, int | str | types.NoneType):
        return item
    if isinstance(item, tuple):
        return {"tuple": serialize_elements(item)}
    if isinstance(item, list):
        return {"list": serialize_elements(item)}
    if isinstance(item, dict):
        return {"dict": item}
    if isinstance(item, bytes):
        return {"bytes": item.hex()}
    if isinstance(item, types.MappingProxyType):
        item_dict = dict(item)
        for key in item_dict.keys():
            item_dict[key] = serialize(item_dict[key])
        print("you what, idiot?")
        return item_dict

    if isinstance(item, types.CodeType):
        return {"code": serialize_pub_attribs(item)}
    if isinstance(item, types.FunctionType):
        return {"func": serialize(item.__code__)}
    if isinstance(item, type):
        attribs_dict = dict(item.__dict__)
        for key in attribs_dict.keys():
            attribs_dict[key] = serialize(attribs_dict[key])
        attribs_dict['__annotations__'] = None
        return {"type": {"name": item.__name__, "attribs": attribs_dict}}

    if (getmodule(type(item)).__name__ in sys.builtin_module_names or
        getmodule(type(item)).__name__ == 'importlib._bootstrap' or
            getmodule(type(item)).__name__ == '_sitebuiltins'):
        return None

    obj_dict = serialize(item.__dict__)
    obj_type = serialize(type(item))
    return {"object": {"obj_type": obj_type, "obj_dict": obj_dict}}


def deserialize(item: dict[str, any]) -> any:
    """Deserialize item from 'dict[str, any]'."""
    if not isinstance(item, dict):
        return item

    for (key, value) in item.items():
        if key =='tuple':
            if value is None:
                return ()
            return tuple(deserialize(element) for element in value.values())

