class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            index = i
            while (stack and stack[-1][1] > heights[i]):
                index = stack[-1][0]
                maxArea = max(maxArea, (i-index)*stack[-1][1])
                stack.pop()
            stack.append((index, heights[i]))
        for i in range(len(stack)):
            maxArea = max(maxArea, (len(heights)-stack[-1][0])*stack[-1][1])
            stack.pop()
        return maxArea
        