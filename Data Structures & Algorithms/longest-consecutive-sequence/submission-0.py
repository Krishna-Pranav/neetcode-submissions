class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxlen = 0
        for num in setNums:
            l = 1
            if num-1 not in setNums:
                while num+1 in setNums:
                    num+=1
                    l+=1
            maxlen = max(l, maxlen)
        return maxlen
        