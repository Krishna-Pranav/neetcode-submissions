class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            a, b, c = nums[l], nums[m], nums[r]
            if b == target:
                return m
            elif a <= b:
                if a <= target < b:
                    r = m-1
                else:
                    l = m+1
            else:
                if b < target <= c:
                    l = m+1
                else:
                    r = m-1
        return -1