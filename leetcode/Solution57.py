from typing import List


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals, index = sorted(intervals), 1
        while index < len(intervals):
            if intervals[index - 1][1] >= intervals[index][0]:
                intervals[index - 1][1] = max(intervals[index - 1][1], intervals[index][1])
                intervals.pop(index)
            else:
                index += 1
        return intervals


if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1, 3], [6, 9]],
                   [2, 5]))
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                   [4, 8]))
