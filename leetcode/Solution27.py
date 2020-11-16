from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                if i != j:
                    nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3, 2, 2, 3],
                          3))
