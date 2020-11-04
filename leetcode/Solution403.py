from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        dic = {1: {1}}
        ad = (-1, 0, 1)
        for i in range(1, len(stones)):
            mid_r = dic.get(stones[i])
            if mid_r:
                for j in mid_r:
                    for k in ad:
                        if j != -k and stones[i] + j + k in stones:
                            if dic.get(stones[i] + j + k):
                                dic[stones[i] + j + k].add(j + k)
                            else:
                                dic[stones[i] + j + k] = {j + k}
        return dic.get(stones[-1]) is not None


if __name__ == '__main__':
    s = Solution()
    # print(s.canCross([0, 1, 3, 4, 5, 7, 9, 10, 12]))
    # print(s.canCross([0, 1, 3, 5, 6, 8, 12, 17]))
    print(s.canCross([0, 1, 3, 6, 10, 15, 16, 21]))
