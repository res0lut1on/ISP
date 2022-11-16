from os import remove
from serializers.serializer_factory import(
    SerializerFabric,
    JsonSerializerFabric,
    XmlSerializerFabric,
    TomlSerializerFabric,
    YamlSerializerFabric
)


def some_thing(fabric: SerializerFabric):
    """Check how serializer works"""
    item = ('test', 'another', {'key': 'val'}, None)
    serializer = SerializerFabric.create_serializer()
    serialized = serializer.dumps(item)
    res = serializer.loads(serialized)
    serializer.dump(res, 'testfile')
    res = serializer.load('testfile')
    assert res == item


def test_thing():
    """Check serializers"""
    some_thing(XmlSerializerFabric)
    some_thing(YamlSerializerFabric)
    some_thing(JsonSerializerFabric)
    remove('testfile')


def test_check():
    """Check exception"""
    XmlSerializerFabric.check()
    JsonSerializerFabric.check()
    YamlSerializerFabric.check()
    TomlSerializerFabric.check()