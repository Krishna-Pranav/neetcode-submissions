class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char for char in s if char.isalnum())
        return clean_s.lower() == (clean_s[::-1]).lower()