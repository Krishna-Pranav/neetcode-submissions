class TimeMap:

    def __init__(self):
        self.tsMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tsMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        items = self.tsMap[key]
        l, r = 0, len(items)-1
        res = ''

        while l <= r:
            mid = l + (r - l) // 2
            if items[mid][0] < timestamp:
                res = items[mid][1]
                l = mid + 1
            elif items[mid][0] > timestamp:
                r = mid - 1
            else:
                return items[mid][1]
        return res