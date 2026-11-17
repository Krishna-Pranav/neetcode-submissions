from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        d1, l, r = Counter(s1), 0, l1
        while r <= l2:
            d2 = Counter(s2[l:r])
            if d1 == d2:
                return True
            l += 1
            r += 1
        return False
            
