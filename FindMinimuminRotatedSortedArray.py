class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        minval = nums[0]
        while(left <= right):
            if(nums[left] < nums[right]):
                minval = min(minval, nums[left])
                break
                
            mid = (left+right)/2
            minval = min(minval, nums[mid])
            if(nums[mid] >= nums[left]):
                left = mid + 1
            else:
                right = mid - 1
        return minval

        