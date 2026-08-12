class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp, rp = 0, len(heights)-1
        maxA = 0
        while lp < rp:
            lval, rval = heights[lp], heights[rp]
            if lval < rval:
                maxA = max(maxA, lval * (rp-lp))
                lp += 1
            else:
                maxA = max(maxA, rval * (rp-lp))
                rp -= 1
        return maxA