import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.m = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.l.append(val)
        type = self.m.get(val)
        self.m[val] = self.m.get(val, 0) + 1
        return not type

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.m.get(val):
            return False
        self.l.remove(val)
        if self.m[val] == 1:
            del self.m[val]
        else:
            self.m[val] -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.l[random.randint(0, len(self.l) - 1)]


if __name__ == '__main__':
    s = RandomizedCollection()
    print(s.insert(1),
          s.insert(1),
          s.insert(2),
          s.getRandom(),
          s.remove(1),
          s.getRandom())
