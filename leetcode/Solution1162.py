from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dis = [[float("inf") for j in range(m+2)] for i in range(n+2)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if grid[i-1][j-1]:
                    dis[i][j] = 0
                else:
                    dis[i][j] = min(dis[i-1][j], dis[i][j-1]) + 1
        res = -1
        for i in range(n, 0, -1):
            for j in range(m, 0, -1):
                if grid[i-1][j-1]:
                    dis[i][j] = 0
                else:
                    dis[i][j] = min(dis[i+1][j]+1, dis[i][j+1]+1, dis[i][j])
                    res = max(dis[i][j], res)
        return res if res != -1 and res != float("inf") else -1

    # BFS ,可惜可惜，python过不了
    # def maxDistance(self, grid: List[List[int]]) -> int:
    #     s = set()
    #     for i in grid:
    #         for j in i:
    #             s.add(j)
    #     if len(s) == 1:
    #         return -1
    #     dx = [1, -1, 0, 0]
    #     dy = [0, 0, 1, -1]
    #     row, col = len(grid), len(grid[0])
    #     result = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j] == 0:
    #                 mapp = [[0] * col for i in range(row)]
    #                 mapp[i][j] = 1
    #                 queue = [(i, j)]
    #                 mid_result = 0
    #                 distance = 0
    #                 while queue and not mid_result:
    #                     for ci in range(len(queue)):
    #                         _ci = queue.pop(0)
    #                         x = _ci[0]
    #                         y = _ci[1]
    #                         for k in range(4):
    #                             if 0 <= x + dx[k] < row and 0 <= y + dy[k] < col:
    #                                 if grid[x + dx[k]][y + dy[k]] == 1:
    #                                     mid_result = distance + 1
    #                                     break
    #                                 if not mapp[x + dx[k]][y + dy[k]]:
    #                                     mapp[x + dx[k]][y + dy[k]] = 1
    #                                     queue.append((x + dx[k], y + dy[k]))
    #                         if mid_result:
    #                             break
    #                     distance += 1
    #                 result = result if result >= mid_result else mid_result
    #     return result


if __name__ == '__main__':
    s = Solution()
    # print(s.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(s.maxDistance([[0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 1]]))
