class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        ps = [(position[i], speed[i]) for i in range(len(speed))]
        ps.sort()
        i = len(speed)-1
        currBlock = 0
        while i >=0:
            val = (target-ps[i][0])/ps[i][1]
            if val > currBlock:
                currBlock = val
                fleets += 1
            i -= 1
        return fleets