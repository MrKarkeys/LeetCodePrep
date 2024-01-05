class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = (left+right)/2
            print(mid, left, right)
            if(nums[mid] == target):
                return mid
            #left side
            if(nums[left] <= nums[mid]):
                if(target > nums[mid] or target < nums[left]):
                    left = mid + 1
                else:
                    right = mid - 1
            #right side
            else:
                if(target < nums[mid] or target > nums[right]):
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

