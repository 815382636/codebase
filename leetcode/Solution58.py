class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.split(' ')
        for i in range(len(ss) - 1, -1, -1):
            if ss[i]:
                return len(ss[i])
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))