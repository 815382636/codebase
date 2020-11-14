from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    # 基于快排
    # def nextPermutation(self, nums: List[int]) -> None:
    #
    #     def quick_sort(l, r):
    #         if l >= r:
    #             return
    #         start, end = l, r
    #         sign = nums[l]
    #         while l < r:
    #             while l < r and nums[r] >= sign:
    #                 r -= 1
    #             nums[l] = nums[r]
    #             while l < r and nums[l] < sign:
    #                 l += 1
    #             nums[r] = nums[l]
    #         nums[l] = sign
    #         quick_sort(start, l - 1)
    #         quick_sort(l + 1, end)
    #
    #     for i in range(len(nums) - 2, -1, -1):
    #         if nums[i] < nums[i + 1]:
    #             quick_sort(i + 1, len(nums) - 1)
    #             for j in range(i+1, len(nums)):
    #                 if nums[j] > nums[i]:
    #                     nums[i], nums[j] = nums[j], nums[i]
    #                     return
    #     for i in range(len(nums) // 2):
    #         nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]


if __name__ == '__main__':
    s = Solution()
    num = [1, 3, 2]
    s.nextPermutation(num)
    print(num)
    num = [2, 3, 1]
    s.nextPermutation(num)
    print(num)
