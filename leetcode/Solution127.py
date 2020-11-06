from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def judge(s1, s2):
            _count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    _count += 1
                if _count > 1:
                    return False
            return _count == 1

        used = [0] * len(wordList)
        used[wordList.index(endWord)] = 2
        queue_st, queue_en, count, sign = [beginWord], [endWord], 1, False

        while not sign and queue_st and queue_en:
            if len(queue_st) <= len(queue_en):
                for i in range(len(queue_st)):
                    it = queue_st.pop(0)
                    for j in range(len(wordList)):
                        if used[j] != 1 and judge(it, wordList[j]):
                            if used[j] == 2:
                                sign = True
                                break
                            else:
                                used[j] = 1
                                queue_st.append(wordList[j])
                    if sign:
                        break
                count += 1
            else:
                for i in range(len(queue_en)):
                    it = queue_en.pop(0)
                    for j in range(len(wordList)):
                        if used[j] != 2 and judge(it, wordList[j]):
                            if used[j] == 1:
                                sign = True
                                break
                            else:
                                used[j] = 2
                                queue_en.append(wordList[j])
                    if sign:
                        break
                count += 1
        return count if sign else 0


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit",
                         "cog",
                         ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(s.ladderLength("lost",
                         "miss",
                         ["most", "mist", "miss", "lost", "fist", "fish"]))
