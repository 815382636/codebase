from typing import List


class Solution:
    # 滑动窗口
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        result, mid = 0, 0
        for i in nums:
            if mid + i > 0:
                mid += i
                if result < mid:
                    result = mid
            else:
                mid = 0
        return result

    # 动态规划
    # def maxSubArray(self, nums: List[int]) -> int:
    #     for i in range(1, len(nums)):
    #         nums[i] = nums[i] + max(nums[i - 1], 0)
    #     return max(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
