from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1
        for i in nums:
            real_i = abs(i)
            if real_i < length + 1 and nums[real_i - 1] > 0:
                nums[real_i - 1] = -nums[real_i - 1]
        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1

    # 时间复杂度O(n),空间复杂度O(n)
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     s = [0] * (len(nums) + 1)
    #     for i in range(len(nums)):
    #         if 0 < nums[i] <= len(nums):
    #             s[nums[i] - 1] = 1
    #     return s.index(0) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
    print(s.firstMissingPositive([1, 1]))
