class OperationA:
    def say(self):
        print('A')


class OperationB:
    def say(self):
        print('B')


class OperationC:
    def say(self):
        print('C')


class Facade:
    def __init__(self):
        self.A = OperationA()
        self.B = OperationB()
        self.C = OperationC()

    def wrapOperation(self):
        self.A.say()
        self.B.say()
        self.C.say()


if __name__ == '__main__':
    f = Facade()
    f.wrapOperation()
