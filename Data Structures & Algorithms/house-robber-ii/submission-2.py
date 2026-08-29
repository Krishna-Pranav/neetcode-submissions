class Solution:
    def findmax(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max1 = self.findmax(nums[:-1])
        max2 = self.findmax(nums[1:])

        return max(max1, max2) 