class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.hp = []
        self.task_to_user = {}
        self.task_to_prio = {}
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)
        # (-pri, -tid)
        # {tid:uid}
        # {tid:pri}

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.hp, (-priority, -taskId))
        self.task_to_user[taskId] = userId
        self.task_to_prio[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.hp, (-newPriority, -taskId))
        self.task_to_prio[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.task_to_user.pop(taskId)
        self.task_to_prio.pop(taskId)

    def execTop(self) -> int:
        while self.hp:
            negprio, negtid = heapq.heappop(self.hp)
            if -negtid not in self.task_to_prio:
                continue
            if self.task_to_prio[-negtid] != -negprio:
                continue
            res = self.task_to_user[-negtid]
            self.rmv(-negtid)
            return res
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()