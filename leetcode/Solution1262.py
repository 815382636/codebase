from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = [0,0,0]
        for i in nums:
            for j in l[:]:
                l[(i+j)%3] = max(l[(i+j)%3],i+j)
        return l[0]