from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
        row, col, count = len(matrix), len(matrix[0]), 0
        remained = [[-1] * col for i in range(row)]

        def count_number(i, j):
            if remained[i][j] == -1:
                remained[i][j] = max([1 + count_number(i + dx[k], j + dy[k]) if 0 <= i + dx[k] < row and 0 <= j + dy[
                    k] < col and matrix[i][j] < matrix[i + dx[k]][j + dy[k]] else 1 for k in range(4)])
            return remained[i][j]

        for i in range(row):
            for j in range(col):
                result = count_number(i, j)
                count = count if count >= result else result
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
