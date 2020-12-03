from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums = sorted(nums)
        for i in nums:
            for j in result[:]:
                r = j + [i]
                if r not in result:
                    result.append(j + [i])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([4, 4, 4, 1, 4]))
