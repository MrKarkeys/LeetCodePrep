class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temp)
        for i in range(len(temp)):
            if(i == 0):
                stack.append(i)
            else:
                while(stack and temp[stack[-1]] < temp[i]):
                    res[stack[-1]] = (i - stack[-1])
                    stack.pop()
                stack.append(i)
        return res

            