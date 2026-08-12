class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrace(curr, perm):
            if len(curr) == 0:
                result.append(perm.copy())
                return
            for i in range(len(curr)):
                perm.append(curr[i])
                ele = curr.pop(i)
                backtrace(curr, perm)
                perm.pop()
                curr.insert(i, ele)
        backtrace(nums, [])
        return result