class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob, n = 0, len(nums)
        if n == 1:
            return nums[0]
        # robbed = [0] * n
        firstH, secondH = nums[0], nums[1]
        maxRob = nums[0]
        for i in range(2, n):
            temp = nums[i] + maxRob
            maxRob = max(maxRob, secondH)
            firstH = secondH
            secondH = temp
        
        return max(maxRob, secondH)