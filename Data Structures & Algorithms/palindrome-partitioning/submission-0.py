class Solution:
    def isPalin(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(partPalin, i):
            # print(partPalin, i)
            if i == len(s):
                result.append(partPalin.copy())
                return
            for j in range(i+1, len(s)+1):
                if self.isPalin(s[i:j]):
                    partPalin.append(s[i:j])
                    backtrack(partPalin, j)
                    partPalin.pop()
        backtrack([], 0)
        return result

