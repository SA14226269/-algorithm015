class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        while (1):
            result = 0
            while(num):
                result += num % 10
                num = num / 10
            if result < 10:
                break
            num = result 
        return result