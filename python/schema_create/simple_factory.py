from abc import ABCMeta, abstractmethod
"""
    简单工厂模式
    CSDN:https://blog.csdn.net/qq_33511971/article/details/109888948
"""

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass


class Cat(Animal):

    def say(self):
        print("MMMMMMMMM")


class Dog(Animal):
    def say(self):
        print("HHHHHHHH")


class AnimalFactory:
    @staticmethod
    def create_animal(type):
        if type == 'cat':
            return Cat()
        elif type == 'dog':
            return Dog()


if __name__ == '__main__':
    cat = AnimalFactory.create_animal('cat')
    cat.say()
    dog = AnimalFactory.create_animal('dog')
    dog.say()
