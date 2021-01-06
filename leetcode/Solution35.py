from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def _search(left, right):
            if left == right:
                return left
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return _search(mid + 1, right)
            else:
                return _search(left, mid)

        if nums[0] >= target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            return _search(0, len(nums))


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6],
                         5))
