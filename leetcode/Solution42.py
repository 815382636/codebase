from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n_max, length, result = 0, len(height), 0
        l_max, r_max = [0], [0]
        for i in range(1, length):
            n_max = n_max if n_max >= height[i - 1] else height[i - 1]
            l_max.append(n_max)
        n_max = 0
        for i in range(length - 2, -1, -1):
            n_max = n_max if n_max >= height[i + 1] else height[i + 1]
            r_max.append(n_max)
        for i in range(length):
            if l_max[i] and r_max[length - 1 - i]:
                m = min(l_max[i], r_max[length - 1 - i])
                if m > height[i]:
                    result += m - height[i]
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([0, 7, 1, 4, 6]))
