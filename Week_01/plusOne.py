class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        count = 1
        while(i >= 0): 
            temp = (digits[i]+count)/10
            digits[i] = (digits[i]+count)%10
            count = temp
            if count == 0:
                break
            i-=1 
        if count == 1:
            return [1] + digits
        return digits