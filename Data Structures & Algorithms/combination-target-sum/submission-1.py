class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        currNums = []
        self.backtrace(result, currNums, 0, nums, target)
        return result
    
    def backtrace(self, result, currNums, i, nums, target):
        if 0 == target and currNums not in result:
            result.append(currNums.copy())
            return
        if i == len(nums) or 0 > target:
            return
        currNums.append(nums[i])
        self.backtrace(result, currNums, i, nums, target-nums[i])
        currNums.pop()
        self.backtrace(result, currNums, i+1, nums, target)

        