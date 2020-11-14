from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mid_dic = {}
        for i, v in enumerate(nums):
            if target - v in mid_dic:
                return [mid_dic[target - v], i]
            mid_dic[v] = i
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15],
                   9))
