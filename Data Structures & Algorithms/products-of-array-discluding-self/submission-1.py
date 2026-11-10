class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = []
        results = []
        mult = 1
        for i, num in enumerate(nums):
            if num == 0:
                zeroes.append(i)
                if len(zeroes) > 1:
                    return [0]*len(nums)
                continue
            mult *= num
        if zeroes:
            results = [0]*len(nums)
            results[zeroes[0]] = mult
        else:
            for num in nums:
                results.append(mult//num)
        return results