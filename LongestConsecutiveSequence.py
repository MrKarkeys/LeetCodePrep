class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        count = 1
        maxcount = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] != nums[i-1]+1:
                    maxcount = max(maxcount, count)
                    count = 1 
                else:
                    count += 1
        return max(maxcount, count)
        