class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        ans = right
        while(left <= right):
            mid = (left+right)/2 
            calch = 0
            for i in piles:
                calch += int(ceil(i/float(mid)))
            if calch <= h:
                ans = min(mid, ans)
                right = mid - 1
            else:
                left = mid + 1
        return ans
        