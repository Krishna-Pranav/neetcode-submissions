class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i, num in enumerate(nums):
            result ^= (i^num)
        return result^len(nums)