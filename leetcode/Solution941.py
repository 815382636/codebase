from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return False
        l, r = 0, len(A) - 1
        while l < r and A[l] < A[l + 1]:
            l += 1
        while l < r and A[r] < A[r - 1]:
            r -= 1
        return l != len(A) - 1 and r != 0 and l == r

    # def validMountainArray(self, A: List[int]) -> bool:
    #     if len(A) <= 2:
    #         return False
    #     l, r = False, False
    #     for i in range(1, len(A)):
    #         if A[i] > A[i - 1]:
    #             l = True
    #         if A[i] < A[i - 1]:
    #             r = True
    #         if A[i] == A[i - 1] or (i + 1 < len(A) and A[i - 1] > A[i] and A[i + 1] > A[i]):
    #             return False
    #     return l and r


if __name__ == '__main__':
    s = Solution()
    print(s.validMountainArray([2, 1]))
