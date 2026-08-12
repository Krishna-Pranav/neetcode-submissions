class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrace(i, currSet):
            result.append(currSet.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                currSet.append(nums[j])
                backtrace(j+1, currSet)
                currSet.pop()
        nums.sort()
        backtrace(0, [])
        return result