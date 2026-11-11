class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for num in store:
            if num-1 not in store:
                cl, cn = 0, num
                while cn in store:
                    cl += 1
                    cn += 1
                res = max(res, cl)
        return res