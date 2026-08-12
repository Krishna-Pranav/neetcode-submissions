class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrace(i, currSet):
            if i == len(nums):
                if currSet not in result:
                    result.append(currSet.copy())
                return
            currSet.append(nums[i])
            backtrace(i+1, currSet)
            currSet.pop()
            backtrace(i+1, currSet)
        nums.sort()
        backtrace(0, [])
        return result