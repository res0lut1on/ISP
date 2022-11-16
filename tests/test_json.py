from types import MappingProxyType
from serializers.json_serializer import JsonSerializer


def mul(first, second):
    return first * second


def test_load():
    """Dumps and loads without excp"""
    serializer = JsonSerializer()
    serialized = serializer.dumps(serializer)
    serializer = serializer.loads(serialized)


def test_func():
    serializer = JsonSerializer()
    serialized = serializer.dumps(mul)
    res = serializer.loads(serialized)
    assert res(8, 6) == 8 * 6


def test_MappingProxyType():
    serializer = JsonSerializer()
    item = {'key': 8, 'key2': 9}
    mpt = MappingProxyType(item)
    serialized = serializer.dumps(mpt)
    serializer.loads(serialized)
