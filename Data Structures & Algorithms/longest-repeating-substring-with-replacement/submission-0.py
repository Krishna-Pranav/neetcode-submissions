from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r, l = 0, 0
        max_char, sol = 0, 0
        chrs = defaultdict(int)
        while r < len(s):
            chrs[s[r]] += 1
            max_char = max(chrs[s[r]], max_char)
            rep = r-l+1-max_char
            if rep > k:
                chrs[s[l]] -=1
                l +=1
            sol = max(sol, r-l+1)
            r += 1
        return sol