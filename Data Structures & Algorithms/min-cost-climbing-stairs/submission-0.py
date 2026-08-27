class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)
        dp[n] = cost[n-1]
        dp[n-1] = cost[n-2]
        for i in range(n-3, -1, -1):
            dp[i+1] = cost[i] + min(dp[i+3], dp[i+2])
        return min(dp[2], dp[1])