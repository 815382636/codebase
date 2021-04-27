class Solution:
    def numTrees(self, n: int) -> int:
        result = [0]*(n + 1)
        result[0] = 1
        result[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                result[i] += result[j - 1] * result[i - j]
        return result[-1]
