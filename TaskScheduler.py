class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        l = [-cnt for cnt in counter.values()]
        heapq.heapify(l)
        q = deque()
        time = 0
        while l or q:
            time += 1
            if l:
                val = 1 + heapq.heappop(l)
                if val != 0:
                    q.append((val, time+n))
            if q and q[0][1] == time:
                heapq.heappush(l, q.popleft()[0])
        return time
