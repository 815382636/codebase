from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        def deal_with(max_value):
            head, _count, _result = -1, 0, [A[0], A[-1]]
            for tail in range(1, len(A)):
                while A[head + 1] / A[tail] < max_value:
                    head += 1
                if head != -1 and _result[0] / _result[1] < A[head] / A[tail]:
                    _result[0], _result[1] = A[head], A[tail]
                _count += head + 1
            return _count, _result

        l, r = 0, 1
        while l + 1e-9 < r:
            mid = l + (r - l) / 2
            count, result = deal_with(mid)
            if count == K:
                return result
            elif count < K:
                l = mid
            else:
                r = mid
        return [A[0], A[-1]]


if __name__ == '__main__':
    s = Solution()
    # print(s.kthSmallestPrimeFraction([1, 2, 3, 5],
    #                                  3))
    # print(s.kthSmallestPrimeFraction([1, 13, 17, 59],
    #                                  6))
    print(s.kthSmallestPrimeFraction([1, 2, 3, 5],
                                     3))
