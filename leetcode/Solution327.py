import bisect
from typing import List


class Solution:
    # 前缀和 + 二分
    # def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    #     if not nums:
    #         return 0
    #     pre_sum, pre_sort, count = [0], [0], 0
    #     for i in nums:
    #         pre_sum.append(pre_sum[-1] + i)
    #     for i in range(1, len(pre_sum)):
    #         low, high = pre_sum[i] - upper, pre_sum[i] - lower
    #         l, r = 0, len(pre_sort) - 1
    #         if pre_sort[r] < low or pre_sort[l] > high:
    #             pre_sort = sorted(pre_sort + [pre_sum[i]])
    #             continue
    #         if pre_sort[l] < low:
    #             _r = r
    #             while l + 1 < _r:
    #                 mid = l + (_r - l) // 2
    #                 if pre_sort[mid] < low:
    #                     l = mid
    #                 else:
    #                     _r = mid
    #             l = _r
    #         if pre_sort[r] > high:
    #             _l = 0
    #             while _l + 1 < r:
    #                 mid = _l + (r - _l) // 2
    #                 if pre_sort[mid] > high:
    #                     r = mid
    #                 else:
    #                     _l = mid
    #             r = _l
    #         count += r - l + 1
    #         pre_sort = sorted(pre_sort + [pre_sum[i]])
    #
    #     return count


    # def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    #     if not nums:
    #         return 0
    #     l = []
    #     count = 0
    #     for i in range(len(nums)):
    #         for j in l[-i:] + [0]:
    #             _in = j + nums[i]
    #             if lower <= _in <= upper:
    #                 count += 1
    #             l.append(_in)
    #     return count

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect.bisect_right(pre, now - lower) - bisect.bisect_left(pre, now - upper)
            bisect.insort(pre, now)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countRangeSum([-2, 5, -1],
                          -2,
                          2))
    print(s.countRangeSum([2147483647, -2147483648, -1, 0],
                          -1,
                          0))
