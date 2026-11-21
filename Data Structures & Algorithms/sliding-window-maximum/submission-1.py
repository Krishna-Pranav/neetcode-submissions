class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        l = 0
        result = []
        for r in range(len(nums)):
            while deq and deq[-1] < nums[r]:
                deq.pop()
            deq.append(nums[r])
            if (r-l+1) == k:
                result.append(deq[0])
                if nums[l] == deq[0]:
                    deq.popleft()
                l += 1
        return result