import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-stone for stone in stones]
        heapq.heapify(stone_heap)
        while len(stone_heap) > 1:
            s1, s2 = heapq.heappop(stone_heap), heapq.heappop(stone_heap)
            if s1 != s2:
                heapq.heappush(stone_heap, s1-s2)
        if len(stone_heap) == 0:
            return 0
        else: return -stone_heap[0]
