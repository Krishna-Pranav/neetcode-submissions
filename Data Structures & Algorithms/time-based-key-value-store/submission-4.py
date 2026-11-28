class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap.keys():
            return ""
        emos = self.timemap[key]
        l, r = 0, len(emos)-1
        res = [-float("inf"), ""]
        while l <= r:
            m = (l+r)//2
            if emos[m][0] == timestamp:
                return emos[m][1]
            if emos[m][0] > res[0] and emos[m][0] < timestamp:
                res[0] = emos[m][0]
                res[1] = emos[m][1]
                l = m + 1
            else:
                r = m-1
        return res[1]