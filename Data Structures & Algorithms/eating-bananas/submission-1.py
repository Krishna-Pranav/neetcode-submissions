import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        lo, hi = 1, piles[-1]
        result = piles[-1]
        while hi >= lo:
            mid = (hi+lo)//2
            count = 0
            for pile in piles:
                count += math.ceil(pile/mid)
            if count <= h:
                result = mid
                hi = mid-1
            else:
                lo = mid+1
        return result