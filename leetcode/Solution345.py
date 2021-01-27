# 'a','o','e','i','u','A','O','E','I','U'
class Solution:
    def reverseVowels(self, s: str) -> str:
        sd = {'a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U'}
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in sd:
                l += 1
            while l < r and s[r] not in sd:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
