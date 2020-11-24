from typing import List


class Solution:

    # 递归回溯
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        dic = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def caculate(r, index):
            if index == len(digits):
                result.append(r)
                return
            val = dic.get(digits[index])
            for i in val:
                caculate((r + i), index + 1)

        caculate('', 0)
        return result

    # 队列回溯
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits: return []
    #     phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     queue = ['']  # 初始化队列
    #     for digit in digits:
    #         for _ in range(len(queue)):
    #             tmp = queue.pop(0)
    #             for letter in phone[ord(digit) - 50]:  # 这里我们不使用 int() 转换字符串，使用ASCII码
    #                 queue.append(tmp + letter)
    #     return queue




if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations(''))
