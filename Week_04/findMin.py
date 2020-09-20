class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        if nums[length-1] > nums[0]:
            return nums[0]
        left = 0
        right = length-1
        #print(nums[length/2])
        while left >= 0 and right >= left:
            mid = (left + right)/2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[left]:
                left = mid+1
            else:
                right = mid-1