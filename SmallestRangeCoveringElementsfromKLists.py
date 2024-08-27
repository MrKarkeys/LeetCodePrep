class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        mmax = float("-inf")
        l1 = []
        for i in range(len(nums)):
            heapq.heappush(l1, (nums[i][0], i, 0))
            mmax = max(mmax, nums[i][0])
        ans = [l1[0][0], mmax]
        while True:
            _, listindex, arrindex = heapq.heappop(l1)
            if len(nums[listindex])-1 == arrindex:
                break
            nextval = nums[listindex][arrindex+1]
            heapq.heappush(l1, (nextval, listindex, arrindex+1))
            mmax = max(mmax, nextval)
            if (mmax - l1[0][0]) < (ans[1] - ans[0]):
                ans = [l1[0][0], mmax]
        return ans
