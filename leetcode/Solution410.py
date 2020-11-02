from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def judge(top):
            s, _m = 0, m
            for num in nums:
                if s + num <= top:
                    s += num
                else:
                    s, _m = num, _m - 1
            return _m > 0

        l, r = max(nums) - 1, sum(nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if judge(mid):
                r = mid
            else:
                l = mid
            print(l, mid, r)
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7, 2, 5, 10, 8],
                       2))
    # print(s.splitArray([1, 4, 4],
    #                    3))
