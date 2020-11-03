from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        result, l_result = 0, 0
        for i in range(1, len(A)):
            l_result = l_result if l_result >= A[i - 1] + i - 1 else A[i - 1] + i - 1
            result = result if result >= A[i] - i + l_result else A[i] - i + l_result
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
