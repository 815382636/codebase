from typing import List

"""
    杨辉三角
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            mr = [1]
            for j in range(1, i, 1):
                mr.append(result[-1][j - 1] + result[-1][j])
            mr.append(1)
            result.append(mr)
        return result
