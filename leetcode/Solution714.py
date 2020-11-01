from typing import List


class Solution:
    # 贪心
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        if not prices or length == 1:
            return 0
        result = 0
        level = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < level:
                level = prices[i]
            elif level + fee < prices[i]:
                result += prices[i] - fee - level
                level = prices[i] - fee
        return result


        # 动态规划
        # result = 0
        # result_list = [[0, -prices[0] - fee], [0, 0]]
        # for i in range(1, length):
        #     x, y = i % 2, (i - 1) % 2
        #     result_list[x][0] = max(result_list[y][0], result_list[y][1] + prices[i])
        #     result_list[x][1] = max(result_list[y][1], result_list[y][0] - fee - prices[i])
        #     result = result if result >= result_list[x][0] else result_list[x][0]
        # return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 3, 2, 8, 4, 9],
                      2))
