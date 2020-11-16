from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.dic = {}
        self.n = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.dic[id] = value
        if self.n == id:
            l = [value]
            self.n += 1
            while self.n in self.dic:
                l.append(self.dic[self.n])
                self.n += 1
            return l
        else:
            return []


if __name__ == '__main__':
    os = OrderedStream(5)
    print(os.insert(3, "ccccc"))
    print(os.insert(1, "aaaaa"))
    print(os.insert(2, "bbbbb"))
    print(os.insert(5, "eeeee"))
    print(os.insert(4, "ddddd"))
