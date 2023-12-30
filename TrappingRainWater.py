class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trapped = 0
        prev = [0] * len(height)
        after = [0] * len(height)

        maxleft = 0
        for i in range(len(height)):
            prev[i] = maxleft
            maxleft = max(height[i], maxleft)

        maxright = 0
        for i in range(len(height)-1, -1, -1):
            after[i] = maxright
            maxright = max(height[i], maxright)
        
        print(prev)
        print(after)
        for i in range(len(height)):
            temp = (min(after[i],prev[i])-height[i])
            if temp > 0:
                trapped += temp 
        return trapped