from abc import ABCMeta, abstractmethod

"""
    工厂方法模式
    CSDN:https://blog.csdn.net/qq_33511971/article/details/109891917
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
    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


if __name__ == '__main__':
    dog = DogFactory().create_animal()
    dog.say()
    cat = CatFactory().create_animal()
    cat.say()
