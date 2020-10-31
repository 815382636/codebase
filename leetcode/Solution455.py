from typing import List


class Solution:
    """
        二分法
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        self.g = g
        self.s = s
        l = 0
        r = len(self.s) if len(self.s) <= len(self.g) else len(self.g)
        while l <= r:
            mid = (l + r) // 2
            if self.check(mid):
                l = mid
            else:
                r = mid
            print(mid,l,r)
        return l

    def check(self, m):
        if m >= len(self.g) or m >= len(self.s):
            return False
        for i in range(m):
            if self.s[len(self.s) - m + i] < self.g[i]:
                return False
        return True
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     g = sorted(g)
    #     s = sorted(s)
    #     num = 0
    #     j = 0
    #
    #     for i in g:
    #         while j < len(s):
    #             if s[j] >= i:
    #                 num += 1
    #                 j += 1
    #                 break
    #             j += 1
    #     return num


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1, 2],
                                [1, 2, 3]))
