class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            t1 = n%2
            result = result*2+t1
            n//=2
        return result