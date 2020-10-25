class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for i in range(num+1)]
        for i in range(1,num+1):
            if i & 1 == 1:
                res[i] = res[i-1]+1
            if i & 1 == 0:
                res[i] = res[i>>1]
        #print(res)
        return res