class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def straightRob(arr):
            l = len(arr)
            if l == 1:
                return arr[0]
            prev, sPrev = arr[0], arr[1]
            maxRob = prev
            for i in range(2, l):
                temp = arr[i] + maxRob
                maxRob = max(maxRob, sPrev)
                prev = sPrev
                sPrev = temp
            
            return max(sPrev, maxRob)

        ans1 = straightRob(nums[:n-1])
        ans2 = straightRob(nums[1:])
        return max(ans1, ans2)