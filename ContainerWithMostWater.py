class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxval = 0
        while(left < right):
            total = min(height[left], height[right]) * (right-left)
            maxval = max(maxval, total)
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return maxval
        