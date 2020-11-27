from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def operate(shu, pie, na):
            j = len(shu)
            if len(shu) == n:
                result.append(shu)
                return
            for i in range(n):
                if i not in shu and i + j not in pie and i - j not in na:
                    operate(shu + [i], pie + [i + j], na + [i - j])

        operate([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in j] for j in result]


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
