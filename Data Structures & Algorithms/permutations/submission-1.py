class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(bag):
            if len(bag) == len(nums):
                res.append(bag.copy())
                return
            for n in nums:
                if n not in bag:
                    bag.append(n)
                    dfs(bag)
                    bag.pop()
        dfs([])
        return res


