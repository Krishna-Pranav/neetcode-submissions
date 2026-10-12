class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []

        def numberBits(num):
            bits = 0
            for i in range(32):
                if num%2:
                    bits+=1
                num//=2
            return bits

        for i in range(n+1):
            results.append(numberBits(i))
        return results