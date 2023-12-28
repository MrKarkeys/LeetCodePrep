class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numlen = len(nums)
        left = 1
        right = 1
        vals = [1] * numlen
        for i in range(1, numlen):
            left *= nums[i-1]
            vals[i] *= left
        for i in range(numlen-2, -1, -1):
            right *= nums[i+1]
            vals[i] *= right
        return vals

        