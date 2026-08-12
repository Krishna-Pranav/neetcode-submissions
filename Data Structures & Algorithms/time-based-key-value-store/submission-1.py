from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.dihh = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dihh.keys():
            self.dihh[key][timestamp] = value
        else:
            self.dihh[key] = SortedDict({timestamp: value})

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dihh.keys():
            return ""
        st, fin = list(self.dihh[key].keys())[0], timestamp
        while st <= fin:
            if fin in self.dihh[key].keys():
                return self.dihh[key][fin]
            fin -= 1
        return ""
