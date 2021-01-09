from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            if i == 0:
                digits.insert(0, 1)
                return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))
