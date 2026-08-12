import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tkn = []
        for i in tokens:
            print(tkn)
            if i in ['+', '-', '*', '/']:
                a = tkn.pop()
                b = tkn.pop()
                if i == '+':
                    tkn.append(a+b)
                elif i == '-':
                    tkn.append(b-a)
                elif i=='*':
                    tkn.append(a*b)
                else:
                    if b/a >= 0:
                        tkn.append(math.floor(b/a))
                    else:
                        tkn.append(math.ceil(b/a))
            else:
                tkn.append(int(i))
        return tkn[-1]