class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp = [[-1 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = 1
        
        # def checkPalin(l, r):
        #     if l >= r:
        #         return 1
        #     if dp[l][r] == -1:
        #         if s[l] == s[r] and checkPalin(l+1, r-1):
        #             dp[l][r] = 1
        #         else:
        #             dp[l][r] = 0
        #     return dp[l][r]

        # result = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if checkPalin(i, j):
        #             result += 1
        
        # return result

        stInd, stLen = 0, 0
        result = 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            l, r = i, i+1
            while l >=0 and r < n and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        return result
