from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        l = [nums[0]]
        for i in range(1, length):
            if nums[i] > l[-1]:
                l.append(nums[i])
            elif nums[i] == l[-1]:
                continue
            else:
                if l[0] >= nums[i]:
                    l[0] = nums[i]
                else:
                    ll, r = 0, len(l) - 1
                    while ll + 1 < r:
                        mid = ll + (r - ll) // 2
                        if l[mid] < nums[i]:
                            ll = mid
                        else:
                            r = mid
                    l[r] = nums[i]
        return len(l)

    # 动态规划
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     l = [1] * len(nums)
    #     result = 1
    #     for i in range(1, len(nums)):
    #         l[i] = max([l[j] for j in range(i) if nums[i] > nums[j]] + [0]) + 1
    #         result = result if result >= l[i] else l[i]
    #     return result


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
