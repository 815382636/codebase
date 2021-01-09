from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        mi, ni = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if nums1[mi] >= nums2[ni]:
                nums1[i] = nums1[mi]
                mi -= 1
            else:
                nums1[i] = nums2[ni]
                ni -= 1
            if mi == -1 or ni == -1:
                break
        if mi == -1:
            nums1[:ni + 1] = nums2[:ni + 1]

        print(nums1)


if __name__ == '__main__':
    s = Solution()
    print(s.merge([1, 2, 3, 0, 0, 0],
                  3,
                  [2, 5, 6],
                  3))
