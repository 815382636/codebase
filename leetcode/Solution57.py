from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        new_list = sorted(intervals)

        def deal_with(index):
            if index + 1 < len(new_list) and new_list[index + 1][0] <= new_list[index][1]:
                new_list[index][1] = max(new_list[index][1], new_list[index + 1][1])
                new_list.pop(index + 1)
                return index
            return index + 1

        i = 0
        while i < len(new_list):
            i = deal_with(i)

        return new_list


if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1, 3], [6, 9]],
                   [2, 5]))
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                   [4, 8]))
