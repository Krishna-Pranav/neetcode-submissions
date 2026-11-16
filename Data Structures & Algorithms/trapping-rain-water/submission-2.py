class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        l, r, maxl, maxr = 0, n-1, 0, 0
        while l < r:
            if height[l] < height[r]:
                if maxl <= height[l]:
                    maxl = height[l]
                else:
                    result += maxl-height[l]
                l += 1
            else:
                if maxr <= height[r]:
                    maxr = height[r]
                else:
                    result += maxr-height[r]
                r -= 1
        return result