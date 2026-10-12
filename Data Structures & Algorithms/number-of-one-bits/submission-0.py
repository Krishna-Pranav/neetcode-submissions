class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        for i in range(32):
            if n % 2:
                bits += 1
            n //= 2
        return bits