class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0 
        i = 0
        earn = 0
        count = 0
        while(i < len(prices)-1):
            if prices[i] <= prices[i+1]:
                count += 1
            else:
                earn += prices[i] - prices[i-count]
                count = 0
            i += 1
        if count > 0 and i == len(prices)-1:
            earn += prices[i] - prices[i-count]
        return earn