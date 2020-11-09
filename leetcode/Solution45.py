from typing import List


class Solution:
    # 贪心
    def jump(self, nums: List[int]) -> int:
        step, maxvalue, end = 0, 0, 0
        for i in range(len(nums) - 1):
            maxvalue = max(maxvalue, i + nums[i])
            if i == end:
                step += 1
                end = maxvalue
        return step

    # 动态规划
    # def jump(self, nums: List[int]) -> int:
    #     row = len(nums)
    #     if row == 1:
    #         return 0
    #     for i in range(row - 2, -1, -1):
    #         if row - 1 - i <= nums[i]:
    #             nums[i] = 1
    #         elif nums[i] == 0:
    #             nums[i] = float('inf')
    #         else:
    #             nums[i] = 1 + min(nums[i + 1:i + nums[i] + 1])
    #     return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
