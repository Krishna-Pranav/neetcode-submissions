class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        def checkPalin(st, en):
            if en <= st:
                return 1
            if s[st] != s[en]:
                return 0
            if dp[st][en] == -1:
                dp[st][en] = checkPalin(st+1, en-1)
            return dp[st][en]
        
        for i in range(n):
            for j in range(i+1, n):
                if checkPalin(i, j):
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        
        for i in range(n-1, 0, -1):
            st, en = 0, i
            while en < n:
                if dp[st][en] == 1:
                    return s[st:en+1]
                st += 1
                en += 1
        return s[0]