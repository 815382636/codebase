from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        result = None
        for i in range(1, rowIndex + 1):
            mr = [1]
            for j in range(1, i, 1):
                mr.append(result[j - 1] + result[j])
            mr.append(1)
            result = mr
        return result
