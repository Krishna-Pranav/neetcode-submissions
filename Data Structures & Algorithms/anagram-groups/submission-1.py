class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            temp = Counter(s)
            text = "".join(char * temp[char] for char in sorted(temp.keys()))
            d[text] = d.get(text, []) + [s]
        return list(d.values())