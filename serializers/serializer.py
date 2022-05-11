from abc import abstractmethod


class Serializer:

    @abstractmethod
    def dumps(self, item: any) -> str:
        """Serialize object, class or function"""

    @abstractmethod
    def loads(self, string: str) -> any:
        """Deserialize object, class or function"""

    def dump(self, item: any, filename: str):
        with open(filename, 'w', encoding='utf8') as file:
            file.write(self.dumps(item))

    def load(self, filename: str):
        """Serialize object, class or function and writeto file"""
        with open(filename, 'r', encoding='utf8') as file:
            string = file.read()
        return self.loads(string)
