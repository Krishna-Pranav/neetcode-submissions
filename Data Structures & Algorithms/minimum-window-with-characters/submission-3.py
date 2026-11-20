from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        ds, dt = {}, Counter(t)
        l, formed, req = 0, 0, len(dt.keys())
        idx, sz = -1, float("inf")
        for r in range(len(s)):
            ds[s[r]] = ds.get(s[r], 0) + 1
            if s[r] in dt and ds[s[r]] == dt[s[r]]:
                formed += 1
            while formed == req:
                if r-l+1 < sz:
                    idx, sz = l, r-l+1
                ds[s[l]] -= 1
                if s[l] in t and ds[s[l]] < dt[s[l]]:
                    formed -= 1
                l += 1
        
        return "" if idx == -1 else s[idx:idx+sz]