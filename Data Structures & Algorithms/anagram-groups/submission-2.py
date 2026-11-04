class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in D:
                D[key] = []
            D[key].append(i)
        return list(D.values())  