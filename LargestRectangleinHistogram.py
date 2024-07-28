class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            start = i
            while(stack and heights[i] < stack[-1][1]):
                val = stack.pop()
                maxArea = max(maxArea, (i-val[0])*val[1])
                start = val[0]
            stack.append((start, heights[i]))
        while(stack):
            lastval = stack.pop()
            maxArea = max(maxArea, (len(heights)-lastval[0])*lastval[1])
        return maxArea
