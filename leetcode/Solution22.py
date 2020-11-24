from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def add(s, left, right):
            if left == right == 0:
                result.append(s)
                return
            elif left == right:
                add(s + '(', left - 1, right)
            elif left == 0:
                add(s + ')', 0, right - 1)
            else:
                add(s + '(', left - 1, right)
                add(s + ')', left, right - 1)

        add('', n, n)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
