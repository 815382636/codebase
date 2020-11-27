from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums, result, length = sorted(nums), [], len(nums)
        sign = [False] * length

        def operate(l):
            if len(l) == length:
                result.append(l)
                return
            for i in range(length):
                if i > 0 and nums[i] == nums[i - 1] and not sign[i - 1]:
                    continue
                if not sign[i]:
                    sign[i] = True
                    operate(l + [nums[i]])
                    sign[i] = False
        operate([])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
