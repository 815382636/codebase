"""
    2的幂写成二进制是0b10000，一个1后边根几个0
    2的幂-1就会是0b1111
    0xaaaaaaaa ---> 8个1010
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0
