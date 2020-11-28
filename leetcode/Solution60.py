class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == k == 1:
            return '1'
        l = [i + 1 for i in range(n)]
        factorial_list, result = [1], ''
        for i in range(2, n):
            factorial_list.append(factorial_list[-1] * i)
        for i in range(len(factorial_list) - 1, -1, -1):
            index = (k + factorial_list[i] - 1) // factorial_list[i]
            k = k % factorial_list[i]
            result += str(l[index - 1])
            l.remove(l[index - 1])
        result += str(l[0])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3,
                           3))
    print(s.getPermutation(1,
                           1))
