class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupNums = set(nums)
        return len(dupNums) != len(nums)