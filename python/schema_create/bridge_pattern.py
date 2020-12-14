"""
    桥接模式
"""
from abc import abstractmethod, ABCMeta


class Human(metaclass=ABCMeta):
    skill = None

    @abstractmethod
    def operation(self):
        pass

    def set_skill(self, skill):
        self.skill = skill


class CSer(Human):
    def operation(self):
        print("我是码农")


class Teacher(Human):
    def operation(self):
        print("我是老师")


class Skill(metaclass=ABCMeta):
    @abstractmethod
    def perform(self):
        pass


class C_Skill(Skill):
    def perform(self):
        print("我会编程")


class T_Skill(Skill):
    def perform(self):
        print("我会教书")


if __name__ == "__main__":
    c_sk = C_Skill()
    t_sk = T_Skill()
    c = CSer()
    c.operation()
    c.set_skill(c_sk)
    c.skill.perform()
    print('-' * 20)
    t = Teacher()
    t.operation()
    t.set_skill(t_sk)
    t.skill.perform()
