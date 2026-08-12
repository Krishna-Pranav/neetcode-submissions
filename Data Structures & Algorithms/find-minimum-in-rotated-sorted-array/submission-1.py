class Solution:
    def findMin(self, nums: List[int]) -> int:
        st, fin = 0, len(nums)-1
        if fin==0:
            return nums[0]
        while fin > st:
            mid = (st+fin)//2
            if nums[fin] < nums[mid]:
                st = mid+1
            else:
                fin = mid
        return nums[st]