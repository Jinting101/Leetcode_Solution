class Router:

    def __init__(self, memoryLimit: int):
        self.cap = memoryLimit
        self.d = deque([])
        self.seen = set()
        self.dest = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.seen:
            return False
        if len(self.d) == self.cap:
            (s, d, t) = self.d.popleft()
            self.seen.remove((s, d, t))
            self.dest[d].popleft()
        self.d.append((source, destination, timestamp))
        self.seen.add((source, destination, timestamp))
        if destination not in self.dest:
            self.dest[destination] = deque([])
        self.dest[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.d:
            return []
        (s, d, t) = self.d.popleft()
        self.seen.remove((s, d, t))
        self.dest[d].popleft()
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest:
            return 0
        lst = self.dest[destination]
        res = (bisect.bisect_right(lst, endTime) - bisect.bisect_left(lst, startTime))
        return res


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)