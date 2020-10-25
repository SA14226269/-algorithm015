class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res,i = 0,0
        while i < 32:
            res <<= 1
            res += n & 1
            n = n >> 1
            i+=1
        return res