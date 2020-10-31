from typing import List
import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = [[]]
        for i in nums:
            for j in l[:]:
                l.append(j+[i])
        return l
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     self.l = [[]]
    #     self.add(nums)
    #     return self.l
    #
    # def add(self, nums):
    #     if not nums:
    #         return
    #     if sorted(nums.copy()) not in self.l:
    #         self.l.append(sorted(nums.copy()))
    #     for i in nums[:]:
    #         nums.remove(i)
    #         self.add(nums)
    #         nums.append(i)


if __name__ == '__main__':
    s = Solution()
    # print(s.subsets([1, 2, 3]))
    print(s.subsets([3,2,4,1]))

