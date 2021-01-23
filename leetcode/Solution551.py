class Solution:
    def checkRecord(self, s: str) -> bool:
        count1, count2 = 0, 0
        for i in s:
            if i == 'A':
                count1 += 1
            if count1 == 2:
                return False
            if i == 'L':
                count2 += 1
            else:
                count2 = 0
            if count2 == 3:
                return False
        return True
