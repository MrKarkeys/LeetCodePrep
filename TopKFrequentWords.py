class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = {}
        ans = []
        map = Counter(waords)
        maxval = max(map.values())
        arr = [[] for i in range(maxval+1)]
        for val, index in map.items():
            heapq.heappush(arr[index], val)
        count = len(arr)-1
        while k > 0:
            if arr[count]:
                ans.append(heapq.heappop(arr[count]))
                k -= 1
            else:
                count -= 1
        return ans
