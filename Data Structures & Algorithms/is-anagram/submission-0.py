class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strDict = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            strDict[s[i]] = strDict.get(s[i], 0) + 1
            strDict[t[i]] = strDict.get(t[i], 0) - 1
        for val in strDict.values():
            if val != 0:
                return False
        return True