from Serializer import Serializer


class SerializerFactory:
    def create_serializer(self):
        return Serializer



s = SerializerFactory()
print(s.create_serializer())