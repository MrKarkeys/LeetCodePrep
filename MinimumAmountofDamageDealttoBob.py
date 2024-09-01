class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        totdam = sum(damage)
        ans = 0
        heap = [0] * len(damage)
        for i in range(len(damage)):
            heap[i] = [-damage[i]/ceil(health[i]/power), damage[i], ceil(health[i]/power)]
        heapq.heapify(heap)
        while heap:
            entry = heapq.heappop(heap)
            ans += totdam * entry[2]
            totdam -= entry[1]
        return ans
