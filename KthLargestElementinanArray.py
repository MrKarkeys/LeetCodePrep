class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            for i in nums:
                if i < pivot:
                    left.append(i)
                elif i > pivot:
                    right.append(i)
                else:
                    mid.append(i)
            if k <= len(right):
                return quickSelect(right, k)
            if len(right) + len(mid) < k:
                return quickSelect(left, k-len(right)-len(mid))
            return pivot 
        
        return quickSelect(nums, k)
