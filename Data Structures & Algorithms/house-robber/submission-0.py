class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob, n = 0, len(nums)
        if n == 1:
            return nums[0]
        robbed = [0] * n
        robbed[0], robbed[1] = nums[0], nums[1]
        maxRob = nums[0]
        for i in range(2, n):
            robbed[i] = nums[i] + maxRob
            maxRob = max(maxRob, robbed[i-1])
        
        return max(maxRob, robbed[-1])