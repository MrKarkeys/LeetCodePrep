class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for i in tokens:
            if (i == "+" or i == "-" 
            or i == "/" or i == "*"):
                val2 = nums.pop()
                val1 = nums.pop()
                comb = 0
                if(i == "+"):
                    comb = val1 + val2
                elif(i == "-"):
                    comb = val1 - val2
                elif(i == "/"):
                    comb = int(float(val1) / val2)
                else:
                    comb = val1 * val2
                nums.append(comb)
            else:
                nums.append(int(i))
        return nums.pop()
