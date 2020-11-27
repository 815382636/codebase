from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s, result = set(nums), []

        def operation(l, mid):
            if not mid:
                result.append(l)
                return
            for i in mid:
                s1 = mid.copy()
                s1.remove(i)
                operation(l + [i], s1)

        operation([], s)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
