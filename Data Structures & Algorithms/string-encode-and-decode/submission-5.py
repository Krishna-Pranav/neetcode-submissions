class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+"#"+s
        return result

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            slen = int(s[i:j])
            strs.append(s[j+1:j+1+slen])
            i = j+1+slen
        return strs