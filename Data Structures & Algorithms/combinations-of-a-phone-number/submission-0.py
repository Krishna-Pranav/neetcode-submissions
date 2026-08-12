class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dialpad = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl" , '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        result = []
        def backtrace(idx, curr):
            if idx == len(digits):
                if curr:
                    result.append("".join(curr))
                return
            for i in dialpad[digits[idx]]:
                curr.append(i)
                backtrace(idx+1, curr)
                curr.pop()
        backtrace(0, [])
        return result
