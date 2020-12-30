class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = int('-' + ''.join(reversed(str(x)))[:-1])
        else:
            x = int(''.join(reversed(str(x))))
        if x > (1 << 31) - 1 or x < - 1 << 31:
            return 0
        return x


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
