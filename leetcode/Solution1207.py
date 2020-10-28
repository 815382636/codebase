from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
        result = set()
        for i in dic.values():
            result.add(i)
        return len(dic) == len(result)
