from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for i in range(n)]
        di_tup = ((0, 1), (1, 0), (0, -1), (-1, 0))
        start, s_x, s_y, di = 1, 0, -1, 0
        while start <= n ** 2:
            x, y = di_tup[di]
            while 0 <= s_x + x < n and 0 <= s_y + y < n and not result[s_x + x][s_y + y]:
                s_x, s_y = s_x + x, s_y + y
                result[s_x][s_y] = start
                start += 1
            di = (di + 1) % 4
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
