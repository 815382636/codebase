from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1 or n == 1:
            return 0 if 1 in [obstacleGrid[i][j] for j in range(n) for i in range(m)] else 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        if obstacleGrid[-1][-1] == -1:
            return 0
        else:
            obstacleGrid[-1][-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1 or obstacleGrid[i][j] == -1:
                    continue
                if i + 1 == m:
                    obstacleGrid[i][j] = obstacleGrid[i][j + 1]
                elif j + 1 == n:
                    obstacleGrid[i][j] = obstacleGrid[i + 1][j]
                elif obstacleGrid[i][j + 1] == -1 or obstacleGrid[i + 1][j] == -1:
                    obstacleGrid[i][j] = max(obstacleGrid[i + 1][j], obstacleGrid[i][j + 1])
                else:
                    obstacleGrid[i][j] = obstacleGrid[i + 1][j] + obstacleGrid[i][j + 1]
        return obstacleGrid[0][0] if obstacleGrid[0][0] != -1 else 0



if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
