class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left,right = 0, len(nums)-1
        while right >= left:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid            
            if nums[left] <= nums[mid] and (target > nums[mid] or target < nums[left]):
                left = mid + 1
            elif target > nums[mid] and target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return -1