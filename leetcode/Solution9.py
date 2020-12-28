class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     x = str(x)
    #     for i in range(len(x) // 2):
    #         if x[i] != x[len(x) - 1 - i]:
    #             return False
    #     return True
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x > 0:
            return False
        c = 0
        while c < x:
            c *= 10
            c += x % 10
            x //= 10
        if c // 10 == x or c == x:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(0))
