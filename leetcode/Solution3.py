class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        result, start, end, mr = 0, 0, 0, 0
        se = set()
        while end < len(s):
            if s[end] not in se:
                mr += 1
                se.add(s[end])
            else:
                ns, start = start, s.find(s[end], start) + 1
                result = result if result >= mr else mr
                for i in range(ns, start -1):
                    se.remove(s[i])
                mr = end - start + 1
            end += 1
        return result if result >= mr else mr


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
