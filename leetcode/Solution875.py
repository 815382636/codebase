from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        r = max(piles)
        if H == len(piles):
            return r
        l = 0

        def judge(eat):
            h = H
            for i in piles:
                h -= (i + eat - 1) // eat
                if h < 0:
                    return False
            return True

        while l + 1 < r:
            mid = l + (r - l) // 2
            if judge(mid):
                r = mid
            else:
                l = mid
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed([3, 6, 7, 11],
                           8
                           ))
