class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [i.lower() for i in s if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9"]
        return l == l[::-1]