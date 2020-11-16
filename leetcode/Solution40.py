from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)

        def caculate(l, sum, remain_l):
            for i in range(len(remain_l)):
                if i > 0 and remain_l[i] == remain_l[i - 1]:
                    continue
                if sum - remain_l[i] < 0:
                    return
                elif sum - remain_l[i] == 0:
                    result.append(l + [remain_l[i]])
                else:
                    if i + 1 < len(remain_l):
                        caculate(l + [remain_l[i]], sum - remain_l[i], remain_l[i + 1:])

        caculate([], target, candidates)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5],
                            8))
