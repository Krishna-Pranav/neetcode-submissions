class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [-1] * (n+1)
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        if n < 3:
            return n
        step1, step2 = 1, 2
        for i in range(3, n+1):
            finalStep = step1 + step2
            step1 = step2
            step2 = finalStep
        
        return step2