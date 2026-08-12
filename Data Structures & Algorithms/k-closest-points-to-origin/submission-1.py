import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointHeap = []
        for point in points:
            distance = math.sqrt((point[0])**2+point[1]**2)
            heapq.heappush(pointHeap, (distance, point))
        result = []
        for i in range(k):
            result.append(heapq.heappop(pointHeap))
        return [x[1] for x in result]
