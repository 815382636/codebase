from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        n1, n2 = 0, 0
        while n1 < len(nums1) and n2 < len(nums2):
            while n1 < len(nums1) and nums1[n1] < nums2[n2]:
                n1 += 1
            while n1 < len(nums1) and n2 < len(nums2) and nums2[n2] < nums1[n1]:
                n2 += 1
            if n1 < len(nums1) and n2 < len(nums2) and nums1[n1] == nums2[n2]:
                result.append(nums2[n2])
                n1 += 1
                n2 += 1
        return result
