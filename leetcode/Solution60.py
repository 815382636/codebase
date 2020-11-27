class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l = [i for i in range(n)]
        sign = [False] * n
        self.k, self.result = k, None

        def operate(s):
            if self.k > 0:
                if len(s) == n:
                    self.k -= 1
                    if self.k == 0:
                        self.result = s
                    return
                for i in range(n):
                    if not sign[i]:
                        sign[i] = True
                        operate(s + str(i + 1))
                        if self.k == 0:
                            return
                        sign[i] = False
        operate('')
        return self.result



if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3,
                           3))
