class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        timeToValue = [timestamp, value]
        self.timeMap[key].append(timeToValue)
        
    def get(self, key: str, timestamp: int) -> str:
        lists = self.timeMap[key]
        lists.sort()
        for i in range(len(lists)-1, -1, -1):
            if lists[i][0] <= timestamp:
                return lists[i][1]
        return ''