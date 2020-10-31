class Solution:
    def numIslands(self, grid) -> int:
        class UnionFind:
            def __init__(self, grid):
                row, col = len(grid), len(grid[0])
                self.parent, self.count = [], 0
                self.rank = [0] * row * col
                for i in range(row):
                    for j in range(col):
                        if grid[i][j] == '1':
                            self.parent.append(i * col + j)
                            self.count += 1
                        else:
                            self.parent.append(0)

            def find(self, index):
                if self.parent[index] != index:
                    self.parent[index] = self.find(self.parent[index])
                return self.parent[index]

            def union(self, i, j):
                rootx = self.find(i)
                rooty = self.find(j)
                if rooty != rootx:
                    if self.rank[rooty] > self.rank[rootx]:
                        self.parent[rootx] = self.parent[rooty]
                    elif self.rank[rooty] < self.rank[rootx]:
                        self.parent[rooty] = self.parent[rootx]
                    else:
                        self.parent[rooty] = self.parent[rootx]
                        self.rank[rootx] += 1
                    self.count -= 1

        dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
        row, col = len(grid), len(grid[0])
        uf = UnionFind(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    for k in range(4):
                        if 0 <= i + dx[k] < row and 0 <= j + dy[k] < col and grid[i + dx[k]][j + dy[k]] == '1':
                            uf.union(i * col + j, (i + dx[k]) * col + j + dy[k])
        return uf.count


# def numIslands(self, grid) -> int:
#     dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
#     height, width = len(grid), len(grid[0])
#
#     def caculate(i, j):
#         if grid[i][j] == '1':
#             grid[i][j] = '0'
#             for k in range(4):
#                 if 0 <= i + dx[k] < height and 0 <= j + dy[k] < width:
#                     caculate(i + dx[k], j + dy[k])
#             return 1
#         return 0
#
#     return sum(caculate(i, j) for j in range(width) for i in range(height))


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands(
        [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]]))
