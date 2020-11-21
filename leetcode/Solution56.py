from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals, index = sorted(intervals), 1
        while index < len(intervals):
            if intervals[index - 1][1] >= intervals[index][0]:
                intervals[index - 1][1] = max(intervals[index - 1][1], intervals[index][1])
                intervals.pop(index)
            else:
                index += 1
        return intervals


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 4], [0, 4]]))
