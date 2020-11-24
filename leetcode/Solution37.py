from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i, v in enumerate(board):
            for j, v2 in enumerate(v):
                if v2 == '.':
                    for k in range(1, 10):
                        if self.is_valid(board, i, j, str(k)):
                            v[j] = str(k)
                            if self.solveSudoku(board):
                                return True
                            else:
                                v[j] = '.'
                    return False
        return True

    def is_valid(self, board, i, v, k):
        if k in board[i]:
            return False
        for k2 in board:
            if k == k2[v]:
                return False
        for j in range(9):
            if board[3 * int(i / 3) + int(j / 3)][3 * int(v / 3) + j % 3] == k:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
