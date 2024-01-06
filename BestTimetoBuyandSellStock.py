class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxval = 0
        while(right < len(prices)):
            sub = prices[right] - prices[left]
            if(sub > 0):
                maxval = max(maxval, sub)
            else:
                left = right
            right += 1
        return maxval

        