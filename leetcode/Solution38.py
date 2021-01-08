class Solution:
    def countAndSay(self, n: int) -> str:
        cur = '1'
        for _ in range(1, n):
            pre = cur
            cur = ''
            start = 0
            end = 0
            while end < len(pre):
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1
                cur += str(end - start) + pre[start]
                start = end
        return cur


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))
