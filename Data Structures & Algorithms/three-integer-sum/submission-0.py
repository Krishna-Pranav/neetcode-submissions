class Solution:
    def twoSum(self, nums, target):
        s, e = 0, len(nums)-1
        result = []
        while s<e:
            val = nums[s]+nums[e]
            if val == target:
                result.append([nums[s], nums[e]])
                s+=1
                e-=1
            elif val <target:
                s+=1
            else:
                e-=1
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i, num in enumerate(nums):
            partL = self.twoSum(nums[i+1:], -(num))
            if partL:
                for l in partL:
                    l.append(num)
                    print(l)
                    result.append(l)
        return [list(t) for t in set(tuple(triplet) for triplet in result)]