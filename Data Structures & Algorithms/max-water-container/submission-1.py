class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = -float("inf")
        l, r = 0, len(heights)-1
        while l < r:
            d = r-l
            h = min(heights[l], heights[r])
            maxA = max(maxA, d*h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA