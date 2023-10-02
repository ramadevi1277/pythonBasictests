from abc import ABC,abstractmethod


class AbstCls(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass


class xyz(AbstCls):

    def add(self):
        print(self.value+100)

    def sub(self):
        print(self.value-10)


obj = xyz(200)
obj.add()
obj.sub()


