import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapNums = [-num for num in nums]
        heapq.heapify(heapNums)
        for _ in range(k-1):
            heapq.heappop(heapNums)
        return -heapNums[0]