class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdict = {}
        strlen, st = float("inf"), 0
        best_start = 0
        for ch in t:
            tdict[ch] = tdict.get(ch, 0) + 1
        count = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in tdict and tdict[ch] > 0:
                count += 1
            tdict[ch] = tdict.get(ch, 0) - 1
            while count == len(t):
                if i - st + 1 < strlen:
                    strlen = i - st + 1
                    best_start = st
                tdict[s[st]] += 1
                if tdict[s[st]] > 0:
                    count -= 1
                st += 1
        return "" if strlen == float("inf") else s[best_start:best_start + strlen]