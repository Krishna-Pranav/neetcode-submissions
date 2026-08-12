class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, fin = 0, len(nums)-1
        while st <= fin:
            mid = (fin+st)//2
            if nums[mid]==target:
                return mid
            if nums[fin] < nums[mid]:
                if nums[st]<=target and target<nums[mid]:
                    fin = mid-1
                else:
                    st = mid+1
            else:
                if target>nums[mid] and target<=nums[fin]:
                    st = mid+1
                else:
                    fin = mid-1
        return -1