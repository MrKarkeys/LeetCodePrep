class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def makeparenthesis(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                makeparenthesis(open+1, closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                makeparenthesis(open, closed+1)
                stack.pop()
        
        makeparenthesis(0, 0)
        return res
            
