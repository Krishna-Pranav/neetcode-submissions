from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]
        # n = len(freq.values())
        # sortedFreq = dict(sorted(freq.items(), key=lambda item: item[1]))
        # return list(sortedFreq.keys())[::-1][:k]