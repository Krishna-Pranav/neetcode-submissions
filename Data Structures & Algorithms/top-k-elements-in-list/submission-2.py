class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        sorted_d = dict(sorted(d.items(), key=lambda i:i[1], reverse=True))
        return list(sorted_d.keys())[:k]