from abc import ABCMeta, abstractmethod


class Refrigerator(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass


class Refrigerator1(Refrigerator):
    def use(self):
        print("Haier refrigerator")


class Refrigerator2(Refrigerator):
    def use(self):
        print("Meidi refrigerator")


class Airconditioner(metaclass=ABCMeta):
    @abstractmethod
    def go(self):
        pass


class Airconditioner1(Airconditioner):
    def go(self):
        print("Haier Airconditioner")


class Airconditioner2(Airconditioner):
    def go(self):
        print("Meidi Airconditioner")


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_refrigerator(self):
        pass

    @abstractmethod
    def create_airconditioner(self):
        pass


class Factory1(Factory):

    def create_refrigerator(self):
        return Refrigerator1()

    def create_airconditioner(self):
        return Airconditioner1()


class Factory2(Factory):

    def create_refrigerator(self):
        return Refrigerator2()

    def create_airconditioner(self):
        return Airconditioner2()


if __name__ == '__main__':
    f = Factory1()
    r1 = f.create_refrigerator()
    r1.use()
    r2 = f.create_airconditioner()
    r2.go()

    f = Factory2()
    r1 = f.create_refrigerator()
    r1.use()
    r2 = f.create_airconditioner()
    r2.go()
