from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, self.sign = len(board[0]), len(board), False
        path = [[False] * m for _ in range(n)]
        dir = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def operate(i, j, re):
            if not self.sign and board[i][j] == re[0] and not path[i][j]:
                if len(re) == 1:
                    self.sign = True
                    return
                path[i][j] = True
                for x, y in dir:
                    _x, _y = x + i, y + j
                    if 0 <= _x < n and 0 <= _y < m:
                        operate(_x, _y, re[1:])
                path[i][j] = False

        for i in range(n):
            for j in range(m):
                operate(i, j, word)
                if self.sign:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                  "ABCCED"))
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                  "SEE"))
    print(s.exist([["a"]],
                  "a"))
