class AllOne:

    def __init__(self):
        self.__min_key = 1
        self.__max_key = 2
        self.map = {self.__min_key: "", self.__max_key: ""}

    def inc(self, key: str) -> None:
        if len(self.map) == 2:
            self.map[self.__max_key] = key
            self.map[self.__min_key] = key
        c = self.map.get(key, 0)
        c += 1
        self.map[key] = c
        if self.map[self.map[self.__max_key]] < c:
            self.map[self.__max_key] = key
        if self.map[self.map[self.__min_key]] > c:
            self.map[self.__min_key] = key
        print(self.map)


    def dec(self, key: str) -> None:
        if len(self.map) == 2:
            self.map[self.__max_key] = key
            self.map[self.__min_key] = key
        c = self.map.get(key, 0)
        c -= 1
        
        if c == 0:
            self.map.pop(key)
        else:
            self.map[key] = c
            if self.map[self.map[self.__max_key]] < c:
                self.map[self.__max_key] = key
            if self.map[self.map[self.__min_key]] > c:
                self.map[self.__min_key] = key
        print(self.map)


    def getMaxKey(self) -> str:
        return self.map.get(self.__max_key)

    def getMinKey(self) -> str:
        return self.map.get(self.__min_key)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()