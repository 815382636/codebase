from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        for i in range(length):
            for j in range(i, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(length):
            for j in range(length // 2):
                matrix[i][j], matrix[i][length - 1 - j] = matrix[i][length - 1 - j], matrix[i][j]


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
