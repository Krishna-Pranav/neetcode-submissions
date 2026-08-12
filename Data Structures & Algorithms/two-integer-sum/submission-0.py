class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, num in enumerate(nums):
            if comp.get(target-num, -1) != -1:
                return [comp[target-num], i]
            comp[num] = i