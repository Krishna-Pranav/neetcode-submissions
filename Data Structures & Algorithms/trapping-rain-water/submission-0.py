class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        maxMap = defaultdict(list)

        currMax = -float("inf")
        for i in range(1, len(height)-1):
            currMax = max(currMax, height[i-1])
            maxMap[i].append(currMax)
        
        currMax = -float("inf")
        for i in range(len(height)-2, 0, -1):
            currMax = max(currMax, height[i+1])
            maxMap[i].append(currMax)
        
        water = 0
        for i in range(1, len(height)-1):
            water += max(0, min(maxMap[i])-height[i])
        
        return water