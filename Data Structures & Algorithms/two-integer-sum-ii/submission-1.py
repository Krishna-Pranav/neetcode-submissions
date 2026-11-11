class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(numbers):
            if target-num in d.keys():
                return [d[target-num], i+1]
            if num not in d.keys():
                d[num] = i+1