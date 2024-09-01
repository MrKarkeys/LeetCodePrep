class Solution:
    def maximumSubarrayXor(self, num: List[int], queries: List[List[int]]) -> List[int]:
        nums = [num]
        while len(nums[-1]) != 1:
            nums.append([nums[-1][i] ^ nums[-1][i+1] for i in range(len(nums[-1])-1)])
        for i in range(1, len(nums)):
            for j in range(len(nums[i])):
                nums[i][j] = max(nums[i][j], nums[i-1][j], nums[i-1][j+1])
        return [nums[r-l][l] for l, r in queries]

