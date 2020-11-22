import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        result = [[1 if j == n - 1 or i == m - 1 else 0 for j in range(n)] for i in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if not result[i][j]:
                    result[i][j] = result[i + 1][j] + result[i][j + 1]
        return result[0][0]

    # 排列组合
    # def uniquePaths(self, m: int, n: int) -> int:
    #     return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))



if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3,
                        7))
