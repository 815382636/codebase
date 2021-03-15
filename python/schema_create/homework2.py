from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def handle(self):
        pass


class Suspend(State):

    def handle(self):
        print("暂停中")


class Play(State):

    def handle(self):
        print("正在播放")


class Context:

    def __init__(self):
        self.state = [Suspend(), Play()]
        self.sign = 0

    def mid(self):
        self.sign = (self.sign + 1) % 2
        self.state[self.sign].handle()

    def left(self):
        self.sign = 1
        print("正在快退", end='---')
        self.state[self.sign].handle()

    def right(self):
        self.sign = 1
        print("正在快进", end='---')
        self.state[self.sign].handle()


def main():
    con = Context()
    con.mid()
    con.mid()
    con.mid()
    con.left()
    con.right()
    con.mid()


if __name__ == '__main__':
    main()
