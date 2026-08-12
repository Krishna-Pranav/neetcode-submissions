class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = "".join(sorted(s1))
        m, n = len(s1c), len(s2)
        for i in range(n-m+1):
            if s1c == "".join(sorted(s2[i:i+m])):
                return True
        return False