class Solution:
    # 二进制解法
    def totalNQueens(self, n: int) -> int:
        self.num = 0

        def caculate(row, col, bie, na):
            if row > n:
                self.num += 1
                return
            sheng = (~(col | bie | na)) & ((1 << n) - 1)
            while sheng > 0:
                s = sheng & -sheng
                caculate(row + 1, s | col, (bie | s) >> 1, (na | s) << 1)
                sheng = sheng & (sheng - 1)

        caculate(1, 0, 0, 0)
        return self.num

    # def totalNQueens(self, n: int) -> int:
    #     self.result = 0
    #
    #     def operate(shu, pie, na):
    #         j = len(shu)
    #         if len(shu) == n:
    #             self.result += 1
    #             return
    #         for i in range(n):
    #             if i not in shu and i + j not in pie and i - j not in na:
    #                 operate(shu + [i], pie + [i + j], na + [i - j])
    #
    #     operate([], [], [])
    #     return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(4))
