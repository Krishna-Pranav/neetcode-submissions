class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        d = {s[0]: 0}
        st, fn = 0, 0
        maxlen = 1
        for i in range(1, len(s)):
            if s[i] not in d or d[s[i]] < st:
                d[s[i]] = i
                fn = i
            else:
                maxlen = max(maxlen, fn-st+1)
                st = d[s[i]] + 1
                d[s[i]] = i
                fn = i
        return max(maxlen, fn-st+1)