class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, -num)

    def findMedian(self) -> float:
        heap_copy = self.heap.copy()
        n = len(heap_copy)
        if n%2 != 0:
            for _ in range(n//2):
                heapq.heappop(heap_copy)
            return -heapq.heappop(heap_copy)
        else:
            for _ in range(n//2-1):
                heapq.heappop(heap_copy)
            m1 = -heapq.heappop(heap_copy)
            m2 = -heapq.heappop(heap_copy)
            return (m1+m2) / 2
        