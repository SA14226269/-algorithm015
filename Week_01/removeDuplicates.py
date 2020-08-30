class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newlen = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[newlen] = nums[i+1]
                newlen += 1
        return newlen