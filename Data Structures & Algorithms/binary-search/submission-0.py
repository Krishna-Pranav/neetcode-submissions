class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi, lo = len(nums)-1, 0
        while hi >= lo:
            mid = (hi+lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        return -1