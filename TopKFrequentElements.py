class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        frq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for i, c in count.items():
            frq[c].append(i)

        res = []
        for i in range(len(frq)-1, 0, -1):
            for j in frq[i]:
                res.append(j)
                if(len(res) == k):
                    return res
