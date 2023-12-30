class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        arr = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while(left < right):
                threesum = nums[left]+nums[right]+nums[i]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    arr.append((nums[i], nums[left], nums[right]))
                    left += 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1
        return arr
                
                
