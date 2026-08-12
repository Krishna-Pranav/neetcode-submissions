class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs=[]
        for s in strs:
            temp=list(s)
            temp2=[chr(ord(t)+1) for t in temp]
            t="".join(temp2)
            encoded_strs.extend([t,"o_o"])
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        strs=list(s.split("o_o"))
        strs.pop()
        decoded_strs=[]
        for ds in strs:
            temp=list(ds)
            temp2=[chr(ord(t)-1) for t in temp]
            t="".join(temp2)
            decoded_strs.append(t)
        return decoded_strs