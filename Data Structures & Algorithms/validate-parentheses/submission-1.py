class Solution:
    def isValid(self, s: str) -> bool:
        paras = {'{':'}', '[':']', '(':')'}
        l = []
        for ch in s:
            if ch in paras.keys():
                l.append(ch)
            else:
                if l and ch == paras[l[-1]]:
                    l.pop()
                else:
                    return False
        if l:
            return False
        return True