from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        def deal_with(index):
            if index + 1 < len(intervals) and intervals[index + 1][0] <= intervals[index][1]:
                intervals[index][1] = max(intervals[index][1], intervals[index + 1][1])
                intervals.pop(index + 1)
                return index
            return index + 1

        i = 0
        while i < len(intervals):
            i = deal_with(i)

        return intervals


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 4], [0, 4]]))
