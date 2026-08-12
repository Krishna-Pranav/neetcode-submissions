class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroInds = []
        totalProd = 1
        result = []
        for i, num in enumerate(nums):
            if num == 0:
                zeroInds.append(i)
            else:
                totalProd *= num
            if len(zeroInds) > 1:
                return [0]*len(nums)

        for num in nums:
            if num == 0:
                result.append(totalProd)
            elif len(zeroInds) > 0:
                result.append(0)
            else:
                result.append(totalProd//num)
        return result