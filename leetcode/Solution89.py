from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
                # print(res)
            head <<= 1
            # print(head)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(5))
