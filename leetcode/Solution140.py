from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 先判断一下s中每一个字母是否都在wordDict中
        if any([i not in set("".join(wordDict)) for i in s]):
            return []
        self.wordDict = wordDict
        self.l = []
        self.caculate(s, '')
        return self.l

    def caculate(self, s, midl):
        if s == '':
            self.l.append(midl[:-1])
        for i in self.wordDict:
            if s.startswith(i):
                self.caculate(s[len(i):], midl + i + " ")


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("catsanddog",
                      ["cat", "cats", "and", "sand", "dog"]))
