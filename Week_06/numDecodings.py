class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: 
            return 0
        if s[0] == '0':
            return 0
        if n == 1:
            if s[0] != '0':
                return 1
            return 0
        pre,cur = 1,1 
        temp = 0
        for i in range(1,n):
            temp = cur
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    cur = pre
                else:
                    return 0
            elif s[i-1] == '1' or (s[i-1] == '2'  and s[i] >= '1' and s[i] <= '6'):
                cur = cur + pre
            pre = temp
        return cur