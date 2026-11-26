class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = float("inf")
        while l <= r:
            m = (r+l)//2
            a, b, c = nums[l], nums[m], nums[r]
            if b < res:
                res = b
            if b >= a and b > c:
                l = m+1
            else:
                r = m-1
        return res