class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for i in s:
            dic1[i] = dic1.get(i, 0) + 1
        for i in t:
            dic2[i] = dic2.get(i, 0) + 1
        return dic1 == dic2

    # def isAnagram(self, s: str, t: str) -> bool:
    #     dic1 = {}
    #     for i in s:
    #         dic1[i] = dic1.get(i, 0) + 1
    #     for i in t:
    #         if i in dic1:
    #             if dic1[i] == 1:
    #                 del dic1[i]
    #             else:
    #                 dic1[i] -= 1
    #         else:
    #             return False
    #     if dic1 == {}:
    #         return True
    #     return False


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram",
                      "nagaram"))
