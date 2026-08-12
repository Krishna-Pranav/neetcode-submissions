class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, fin = 0, -1
        cdict = {}
        maxL = 0
        for i, c in enumerate(s):
            if c in cdict.keys() and st <= cdict[c]:
                maxL = max(maxL, fin-st+1)
                st = cdict[c]+1
                fin = i
                cdict[c] = i
            else:
                cdict[c] = i
                fin = i
        return max(maxL, fin-st+1)