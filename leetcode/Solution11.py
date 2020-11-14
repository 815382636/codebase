from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, result = 0, len(height) - 1, 0
        while l < r:
            h = min(height[l], height[r])
            result = max(result, (r - l) * h)
            if h == height[l]:
                l += 1
            else:
                r -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
