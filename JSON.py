import json
from Serializer import Serializer


class JSON(Serializer):
    def dumb(obj, fp):
        pass
    def dumps(obj):
        pass
    def load(fp):
        pass
    def loads(self, s):
        super().loads()
        pass 
    pass

class schoolBoy:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name

data = {}
data['people'] = []
data['people'].append({
    'name':'Scott',
    'website':'lurkmore.ru',
    'from':'Saratov'
})
with open('LAB2\data.txt', 'w') as outfile:
    json.dump(data, outfile)
#with open("LAB2\data.txt", encoding="utf-8") as fh:
 #   fh.write()
