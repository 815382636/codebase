from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)

        def caculate(l, sum, remain_l):
            for i in range(len(remain_l)):
                if sum - remain_l[i] < 0:
                    return
                elif sum - remain_l[i] == 0:
                    result.append(l + [remain_l[i]])
                else:
                    caculate(l + [remain_l[i]], sum - remain_l[i], remain_l[i:])

        caculate([], target, candidates)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7],
                           7))
    print(s.combinationSum([1],
                           2))
