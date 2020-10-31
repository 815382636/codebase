from typing import List


class Solution:
    """
    二分
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not s or not nums or sum(nums) < s:
            return 0
        # 求前缀和
        self.nums_sum = [0]
        for i, v in enumerate(nums):
            self.nums_sum.append(self.nums_sum[i] + v)
        l, r = 0, len(nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.check(mid, s):
                r = mid
            else:
                l = mid
        return r

    def check(self, index, s):
        for i in range(index, len(self.nums_sum)):
            if self.nums_sum[i] - self.nums_sum[i - index] >= s:
                return True
        return False

    """
    滑动窗口
    """
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     if not s or not nums or sum(nums) < s:
    #         return 0
    #     result, count, _s, left, right = 0, 0, 0, 0, 0
    #     nums_len = len(nums)
    #     while right < nums_len:
    #         while _s < s and right < nums_len:
    #             _s += nums[right]
    #             right += 1
    #             count += 1
    #         if _s < s:
    #             break
    #         result = (result if result <= count else count) if result else count
    #         while _s >= s:
    #             _s -= nums[left]
    #             left += 1
    #             count -= 1
    #         result = result if result <= (count + 1) else (count + 1)
    #         if result == 1:
    #             return result
    #     return result


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(213,
                           [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))
