from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dihh = [-val for val in Counter(tasks).values()]
        heapq.heapify(dihh)
        q = deque()
        time = 0
        while dihh or q:
            if q:
                i, j = q[0]
                if time == j:
                    heapq.heappush(dihh, i)
                    q.popleft()
            temp = 0
            if dihh:
                temp = heapq.heappop(dihh)+1
            time += 1
            if temp != 0:
                q.append((temp, time+n))
        return time