class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, maxlen = 0, 0
        char_set = set()
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[st])
                st += 1
            char_set.add(s[i])
            maxlen = max(maxlen, i-st+1)
        return maxlen