from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                if i != j:  # 优化，防止原地复制
                    nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))
