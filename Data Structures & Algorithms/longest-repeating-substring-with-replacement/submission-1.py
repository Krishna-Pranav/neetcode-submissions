class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        temp = {}
        while l <= r and r < len(s):
            temp[s[r]] = 1 + temp.get(s[r], 0)
            window = r - l + 1
            if window - max(temp.values()) <= k:
                res = max(res, window)
            else:
                temp[s[l]] -= 1
                l += 1
            r += 1
        return res