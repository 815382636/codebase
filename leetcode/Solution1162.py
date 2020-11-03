from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        s = set()
        for i in grid:
            for j in i:
                s.add(j)
        if len(s) == 1:
            return -1
        self.grid = grid
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]
        self.row, self.col = len(grid), len(grid[0])
        self.result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.caculate(i, j, 0)
        return self.result

    def caculate(self, i, j, distance):
        sign = False
        sign_list = [False, False, False, False]
        for k in range(4):
            if 0 <= self.dx[k] + i < self.row and 0 <= self.dy[k] + j < self.col and not self.grid[self.dx[k] + i][
                self.dy[k] + j]:
                self.grid[self.dx[k] + i][self.dy[k] + j] = 1
                sign = True
                sign_list[k] = True
        if sign:
            distance += 1
            for k in range(4):
                if 0 <= self.dx[k] + i < self.row and 0 <= self.dy[k] + j < self.col:
                    self.caculate(self.dx[k] + i, self.dy[k] + j, distance)
            for k in range(4):
                if sign_list[k]:
                    self.grid[self.dx[k] + i][self.dy[k] + j] = 0
        else:
            self.result = self.result if self.result >= distance else distance


if __name__ == '__main__':
    s = Solution()
    print(s.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
