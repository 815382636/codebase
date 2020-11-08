from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        row, col = len(grid), len(grid[0])
        k = min(k, row + col - 3)
        path, queue, count = [(0, 0, k)], [(0, 0, k)], 0
        while queue:
            for i in range(len(queue)):
                point = queue.pop(0)
                if point[0] == row - 1 and point[1] == col - 1:
                    return count
                x, y, _k = point[0], point[1], point[2]
                for j in range(4):
                    if 0 <= dx[j] + x < len(grid) and 0 <= dy[j] + y < len(grid[0]):
                        tup = (x + dx[j], y + dy[j], _k - grid[dx[j] + x][dy[j] + y])
                        if tup[2] >= 0 and tup not in path:
                            path.append(tup)
                            queue.append(tup)
            count += 1
        return -1
    # def shortestPath(self, grid: List[List[int]], k: int) -> int:
    #     if not any(grid):
    #         return -1
    #     m, n = len(grid), len(grid[0])
    #     k = min(k, m + n - 3)
    #     q = [(0, 0, k, 0)]
    #     visited = {(0, 0, k)}
    #     while q:
    #         x, y, rest, steps = q.pop(0)
    #         print(x, y, rest, steps)
    #         if x == m - 1 and y == n - 1:
    #             return steps
    #         for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
    #             print(nx, ny)
    #             if 0 <= nx < m and 0 <= ny < n:
    #                 nk = rest - grid[nx][ny]
    #                 if nk < 0 or (nx, ny, nk) in visited:
    #                     continue
    #                 q.append((nx, ny, nk, steps + 1))
    #                 visited.add((nx, ny, nk))
    #     return -1


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]],
                         1))
