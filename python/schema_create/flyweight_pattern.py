class FlyWeight:
    def __init__(self, s):
        self.s = s

    def say(self):
        print(f"{self.s}:我是池子的一员")


class FlyWeightFactory:
    def __init__(self):
        self.d = {}

    def getFlyWeight(self, s):
        if s in self.d:
            return self.d[s]
        else:
            r = FlyWeight(s)
            self.d[s] = r
            return r


if __name__ == '__main__':
    f = FlyWeightFactory()
    d1 = f.getFlyWeight('one')
    d1.say()
    d2 = f.getFlyWeight('two')
    d2.say()
    d3 = f.getFlyWeight('one')
    d3.say()
