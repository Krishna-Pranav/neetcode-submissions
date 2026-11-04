class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        secNums = {}
        for i, num in enumerate(nums):
            if target-num in secNums.keys():
                return [secNums[target-num], i]
            secNums[num] = i
