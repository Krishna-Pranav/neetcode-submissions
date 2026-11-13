class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        def twoSum(nums, start, target):
            l, r = start, len(nums)-1
            pairs = []
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    pairs.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
            return pairs

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            pairs = twoSum(nums, i+1, -nums[i])
            for pair in pairs:
                results.append([nums[i]] + pair)

        return results