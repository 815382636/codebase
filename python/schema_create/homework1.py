from abc import ABCMeta, abstractmethod


class Bus:

    def __init__(self):
        self.messageMap = {}

    def register(self, event, ele):
        if event in Bus.messageMap:
            self.messageMap[event].append(ele)
        else:
            self.messageMap[event] = [ele]

    def on(self, e, msg):
        e.callback(msg)

    def off(self, event, ele):
        if event in self.messageMap and ele in self.messageMap[event]:
            self.messageMap[event].remove(ele)

    def emit(self, event, msg):
        if event in self.messageMap:
            for e in self.messageMap[event]:
                self.on(e, msg)


class Element(metaclass=ABCMeta):

    @abstractmethod
    def callback(self, msg):
        pass

    @abstractmethod
    def call(self, bus, event, msg):
        pass


class ConcreteElement(Element):

    def __init__(self, name):
        self.name = name

    def callback(self, msg):
        print(f"I am {self.name}, callback message : {msg}")

    def call(self, bus, event, msg):
        bus.emit(event, msg)


def main():
    bus = Bus()
    e1 = ConcreteElement('element1')
    e2 = ConcreteElement('element2')
    bus.register('test', e1)

    # 测试 emit - on - callback
    e2.call(bus, 'test', 'come from e2')

    # 测试 off
    print(Bus.messageMap)
    bus.off('test', e1)
    print(Bus.messageMap)


if __name__ == '__main__':
    main()
