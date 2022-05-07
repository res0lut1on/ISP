import inspect


class Pudge:
    def __init__(self, sila):
        self.sila = sila

    sila = 100

    def dismember(self):
        print("fresh meat")


meat = Pudge(1)
str1 = inspect.getmembers(meat, predicate=inspect.ismethoddescriptor)
str2 = inspect.getdoc(Pudge.dismember)
print(str2)
