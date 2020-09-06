class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        maxCount, i = [], 0
        while(i < len(nums)-k+1):
            maxCount.append(max(nums[i:i+k]))
            i+=1
        return maxCount