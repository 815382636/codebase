from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if any([i not in set(''.join(wordDict)) for i in s]):
            return False
        l = [0] * (len(s) + 1)
        l[0] = 1
        for i in range(len(l)):
            for j in wordDict:
                if i >= len(j) and l[i - len(j)] == 1 and s[i - len(j):].startswith(j):
                    l[i] = 1
        print(l)
        return l[-1] == 1


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode",
                      ["leet", "code"]))
