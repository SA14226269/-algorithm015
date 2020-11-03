class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        if len(nums) == 1: return 1
        dp = [0 for i in range(len(nums))]
        #print(dp)
        for i in range(len(nums)):
            dp[i] = 1      
        for i in range(len(nums)):           
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)