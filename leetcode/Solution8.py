import re


class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("+-12"))
