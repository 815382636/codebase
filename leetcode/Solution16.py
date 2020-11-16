from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = None
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                mid_result = nums[i] + nums[l] + nums[r] - target
                if not mid_result:
                    return target
                if mid_result < 0:
                    l += 1
                else:
                    r -= 1
                result = mid_result + target if result is None or abs(result - target) > abs(mid_result) else result

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4],
                            1))
