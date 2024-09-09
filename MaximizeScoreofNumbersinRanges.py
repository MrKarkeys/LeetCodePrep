class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def isgood(nums, mid):
            prev = nums[0]
            for i in range(1, len(nums)):
                nextval = max(nums[i], mid+prev)
                if nextval > nums[i]+d:
                    return False
                prev = nextval
            return True
        start.sort()
        l = 0
        r = start[-1]-start[0]+d
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if isgood(start, mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1   
        return ans

        
