import itertools
from typing import List, Tuple, Any


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def operate(l, alive):
            m, m1 = len(l), n - alive + 1
            if m == k:
                result.append(l)
                return
            if m + n < k:
                return
            for i in range(alive, n + 1):
                operate(l + [i], i + 1)

        operate([], 1)
        return result

    # Python一行
    # def combine(self, n: int, k: int) -> List[Tuple[Any, ...]]:
    #     return list(itertools.combinations(range(1, n + 1), k))

    # 子集 + 剪枝
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     result = [[]]
    #     l = (i + 1 for i in range(n))
    #     for i in range(1, n + 1):
    #         for j in result[:]:
    #             if len(j) < k:
    #                 result.append(j + [i])
    #     return [i for i in result if len(i) == k]


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,
                    2))
