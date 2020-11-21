from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col, result, di, px, py = len(matrix), len(matrix[0]), [], 0, 0, -1
        sign = [[0] * col for i in range(row)]
        go = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while len(result) < row * col:
            x, y = go[di][0], go[di][1]
            while 0 <= px + x < row and 0 <= py + y < col and not sign[px + x][py + y]:
                px, py = px + x, py + y
                result.append(matrix[px][py])
                sign[px][py] = 1
            di = (di + 1) % 4
        return result

    # 经典
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     res = []
    #     while matrix:
    #         res += matrix.pop(0)
    #         matrix = list(zip(*matrix))[::-1]
    #     return res


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
