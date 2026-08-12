class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        lParan, rParan = n, n
        def backtrace(sList):
            nonlocal lParan, rParan
            if lParan == 0 and rParan == 0:
                result.append("".join(sList))
                return
            # if lParan == 0:
            #     while rParan > 0:
            #         sList.append(')')
            #         rParan -= 1
            #     result.append("".join(sList))
            if rParan > lParan:
                sList.append(')')
                rParan -= 1
                backtrace(sList)
                sList.pop()
                rParan += 1
            if lParan > 0:
                sList.append('(')
                lParan -= 1
                backtrace(sList)
                sList.pop()
                lParan += 1
        backtrace([])
        return result
