from abc import abstractmethod
from ISP.serializers.Serializer import Serializer


class SerializerFabric:

    @staticmethod
    @abstractmethod
    def create_serializer() -> Serializer:
        return Serializer

    @classmethod
    def check(cls):
        ser = cls.create_serializer()
        string = ser.dumps(cls)
        ser.loads(string)
