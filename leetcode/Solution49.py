from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for st in strs:
            key = "".join(sorted(st))
            if key not in mp:
                mp[key] = [st]
            else:
                mp[key].append(st)

        return list(mp.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
