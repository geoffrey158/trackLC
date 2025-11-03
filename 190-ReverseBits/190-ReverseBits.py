# Last updated: 11/2/2025, 8:23:33 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

        #time complexity:O(1))
        #space complexity:O(1)