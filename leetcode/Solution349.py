from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    s = Solution()
    print(s.intersection([1, 2, 2, 1],
                         [2, 2]))
