from abc import abstractmethod
import serializers


class SerializerFabric:

    @staticmethod
    @abstractmethod
    def create_serializer() -> serializers.Serializer:
        """Create serializer"""""

    @classmethod
    def check(cls):
        """Use serializer"""
        ser = cls.create_serializer()
        string = ser.dumps(cls)
        ser.loads(string)


class XmlSerializerFabric(SerializerFabric):

    @staticmethod
    def create_serializer() -> serializers.Serializer:
        return serializers.XmlSerializer()


class YamlSerializerFabric(SerializerFabric):

    @staticmethod
    def create_serializer() -> serializers.Serializer:
        return serializers.YamlSerializer()


class TomlSerializerFabric(SerializerFabric):

    @staticmethod
    def create_serializer() -> serializers.Serializer:
        return serializers.TomlSerializer()


class JsonSerializerFabric(SerializerFabric):

    @staticmethod
    def create_serializer() -> serializers.Serializer:
        return serializers.JsonSerializer()