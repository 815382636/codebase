from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r, sum, ms = [], 0, 0
        for i in range(len(prices) - 1):
            r.append(prices[i + 1] - prices[i])
        for i in r:
            if i < 0:
                sum = sum if sum > ms else ms
                ms += i
                if ms < 0:
                    ms = 0
            else:
                ms += i
        return sum if sum > ms else ms


def main():
    print(Solution().maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    main()
