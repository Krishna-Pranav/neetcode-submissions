class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, k
        result = [max(nums[i:j])]
        while j < len(nums):
            i+=1
            j+=1
            if nums[i-1] == result[-1]:
                result.append(max(nums[i:j]))
            elif nums[j-1] > result[-1]:
                result.append(nums[j-1])
            else:
                result.append(result[-1])
        return result