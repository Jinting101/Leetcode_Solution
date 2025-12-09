class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = {-1:[]}
        self.timemap[key][-1].append(timestamp)
        self.timemap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        if timestamp in self.timemap[key]:
            return self.timemap[key][timestamp]
        idx = bisect.bisect_right(self.timemap[key][-1], timestamp)
        if idx == 0:
            return ""
        return self.timemap[key][self.timemap[key][-1][idx-1]]

        

        
# 1 4 5
# {'foo':{-1:[1, 4], 1:'bar', 4:'bar2'}}
# {'foo':{-1:[5], 5:'bar'}}
# get('foo', 1) - 5 !< 1

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)