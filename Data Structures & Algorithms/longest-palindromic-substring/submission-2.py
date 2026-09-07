class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        stInd, stLen = 0, 0
        for i in range(n):
            st, en = i, i
            while st >=0 and en < n and s[st]==s[en]:
                if en-st+1 > stLen:
                    stLen = en-st+1
                    stInd = st
                st -= 1
                en += 1
            st, en = i, i+1
            while st >= 0 and en < n and s[st]==s[en]:
                if en-st+1 > stLen:
                    stLen = en-st+1
                    stInd = st
                st -= 1
                en += 1
        return s[stInd:stInd+stLen]
