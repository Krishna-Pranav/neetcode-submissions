class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        currSet = []
        self.allsubs(0, nums, currSet, result)
        return result

    def allsubs(self, idx, nums, currSet, result):
        if idx == len(nums):
            result.append(currSet.copy())
            return
        currSet.append(nums[idx])
        self.allsubs(idx+1, nums, currSet, result)
        currSet.pop()
        self.allsubs(idx+1, nums, currSet, result)