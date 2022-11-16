import qtoml
import serializers.serializer_core as core
from serializers.serializer import Serializer


class TomlSerializer(Serializer):

    def dumps(self, item):
        """Serialize obj, cls or func to toml"""
        return qtoml.dumps(core.serialize(item), encode_none=())

    def loads(self, string):
        """Deserialize obj, cls or func to toml"""
        return core.deserialize(qtoml.loads(string))
