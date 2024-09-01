class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        ans = []
        dist = []
        for x, y in queries:
            tot = abs(x)+abs(y)
            heapq.heappush(dist, -tot)
            if len(dist) > k:
                heapq.heappop(dist)
            ans.append(-dist[0] if len(dist) == k else -1)
        return ans
