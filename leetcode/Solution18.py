from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3] < target:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums[j] + nums[i] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[j] + nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] < target:
                    continue
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    mid_result = nums[i] + nums[j] + nums[l] + nums[r]
                    if mid_result == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l + 1 < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l + 1 < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif mid_result < target:
                        l += 1
                    else:
                        r -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2],
                    0))
    print(s.fourSum([0, 0, 0, 0],
                    0))
