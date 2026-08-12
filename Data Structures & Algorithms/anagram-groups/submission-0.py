class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for word in strs:
            temp = "".join(sorted(word))
            if anag.get(temp, 0) == 0:
                anag[temp] = [word]
            else:
                anag[temp].append(word)
        return list(anag.values())