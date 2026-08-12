class LRUCache:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__cache = {}

    def get(self, key: int) -> int:
        value = self.__cache.pop(key, -1)
        if value != -1:
            self.__cache[key] = value
        print("GET: ", value)
        for k, v in self.__cache.items():
            print(k, " : ", v, end=";   ")
        print(end='\n')
        return value

    def put(self, key: int, value: int) -> None:
        self.__cache.pop(key, -1)
        self.__cache[key] = value
        if len(self.__cache) > self.__capacity:
            self.__cache.pop(list(self.__cache.keys())[0])
        print("PUT: ", key, " : ", value)
        for k, v in self.__cache.items():
            print(k, " : ", v, end=";   ")
        print(end='\n')
        