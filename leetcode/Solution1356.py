from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # return sorted(sorted(arr), key=lambda x: bin(x).count("1"))
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


if __name__ == '__main__':
    s = Solution()
    print(s.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(s.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
