class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        identity, curr = defaultdict(int), defaultdict(int)
        if len(s2) < len(s1):
            return False
        for s in s1:
            identity[s] += 1
        for i in range(len(s1)):
            curr[s2[i]] += 1
        if curr == identity:
            return True
        for i in range(len(s1), len(s2)):
            curr[s2[i]] += 1
            curr[s2[i - len(s1)]] -= 1
            if curr[s2[i - len(s1)]] == 0:
                del curr[s2[i - len(s1)]]
            if curr == identity:
                return True
        return False