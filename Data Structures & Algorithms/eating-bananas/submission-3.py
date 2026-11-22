class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = float("inf")
        while l <= r:
            m = l + (r-l)//2
            temp = sum([-(-p//m) for p in piles])
            if temp <= h:
                k = min(k, m)
                r = m-1
            elif temp > h:
                l = m+1
        return k