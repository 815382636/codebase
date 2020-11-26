from abc import abstractmethod


class Builder:
    def __init__(self):
        self._prod = ''

    @abstractmethod
    def buildPartA(self):
        pass

    @abstractmethod
    def buildPartB(self):
        pass

    @abstractmethod
    def buildPartC(self):
        pass

    def getResult(self):
        print(self._prod)


class ConcreteBuilder(Builder):

    def __init__(self):
        super().__init__()

    def buildPartA(self):
        self._prod += 'setA \t'

    def buildPartB(self):
        self._prod += 'setB \t'

    def buildPartC(self):
        self._prod += 'setC \t'


class Director:

    def __init__(self):
        self.__builder = None

    def constuct(self):
        if self.__builder:
            self.__builder.buildPartA()
            self.__builder.buildPartB()
            self.__builder.buildPartC()
            self.__builder.getResult()

    def setBuilder(self, builder):
        self.__builder = builder


if __name__ == '__main__':
    bd = ConcreteBuilder()
    dr = Director()
    dr.setBuilder(bd)
    dr.constuct()
