from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
        length, width, result = len(grid), len(grid[0]), 0
        for i in grid:
            i.insert(0, 0)
            i.append(0)
        grid.insert(0, [0] * (width + 2))
        grid.append([0] * (width + 2))
        for i in range(1, length + 2):
            for j in range(1, width + 2):
                if grid[i][j] == 1:
                    result += [grid[i + dx[k]][j + dy[k]] for k in range(4)].count(0)
        return result
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     if not grid:
    #         return 0
    #     dx, dy = (-1, 0), (0, -1)
    #     length, width, result = len(grid), len(grid[0]), 0
    #     for i in range(length):
    #         for j in range(width):
    #             if grid[i][j] == 1:
    #                 result += 4
    #                 for k in range(2):
    #                     if 0 <= i + dx[k] < length and 0 <= j + dy[k] < width and grid[i + dx[k]][j + dy[k]] == 1:
    #                         result -= 2
    #     return result
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     if not grid:
    #         return 0
    #     dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    #     length, width, result = len(grid), len(grid[0]), 0
    #     for i in range(length):
    #         for j in range(width):
    #             for k in range(4):
    #                 if grid[i][j] == 1:
    #                     if 0 <= i + dx[k] < length and 0 <= j + dy[k] < width and grid[i + dx[k]][j + dy[k]] == 1:
    #                         continue
    #                     result += 1
    #     return result


if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
