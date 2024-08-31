class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i in range(len(points)):
            dist = sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heapq.heappush(heap, (dist, i))
        for i in range(k):
            dist, index = heapq.heappop(heap)
            ans.append(points[index])
        return ans
