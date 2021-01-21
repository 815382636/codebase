class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        sign = 'A' <= word[0] <= 'Z'
        sign1,sign2 = False, False
        for i in range(1, len(word)):
            if not sign:
                if 'A' <= word[i] <= 'Z':
                    return False
            else:
                if 'A' <= word[i] <= 'Z':
                    if sign2:
                        return False
                    sign1 =True
                else:
                    if sign1:
                        return False
                    sign2 = True

        return True