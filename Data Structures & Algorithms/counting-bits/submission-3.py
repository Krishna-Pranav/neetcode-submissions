class Solution:
    def countBits(self, n: int) -> List[int]:
        # results = [0] * (n+1)
        # for i in range(1, n+1):
        #     if i%2 != 0:
        #         results[i] = results[i//2] + 1
        #     else:
        #         results[i] = results[i//2]
        # return results
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp