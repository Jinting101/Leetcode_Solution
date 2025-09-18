class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.cur_tasks = set()
        self.task_to_pri = {}
        self.hp = []
        self.taskpri_to_user = {}

        for user, task, pri in tasks:
            self.cur_tasks.add(task)
            self.task_to_pri[task] = pri
            heapq.heappush(self.hp, (-pri, -task))
            self.taskpri_to_user[(pri, task)] = user

        # set()
        # {task: pri}  task_to_pri
        # [(-pri, -task)]
        # {(pri,task): user}    taskpri_to_user

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.cur_tasks.add(taskId)
        self.task_to_pri[taskId] = priority
        heapq.heappush(self.hp, (-priority, -taskId))
        self.taskpri_to_user[(priority, taskId)] = userId
    

    def edit(self, taskId: int, newPriority: int) -> None:
        user = self.taskpri_to_user[(self.task_to_pri[taskId], taskId)]
        self.taskpri_to_user.pop((self.task_to_pri[taskId], taskId))
        self.task_to_pri[taskId] = newPriority
        self.taskpri_to_user[(newPriority, taskId)] = user
        heapq.heappush(self.hp, (-newPriority, -taskId))
        

    def rmv(self, taskId: int) -> None:
        self.cur_tasks.remove(taskId)
        self.taskpri_to_user.pop((self.task_to_pri[taskId], taskId))
        self.task_to_pri.pop(taskId)

    def execTop(self) -> int:
        while self.hp:
            pri, task = self.hp[0]
            if -task not in self.cur_tasks or self.task_to_pri[-task] != -pri:
                heapq.heappop(self.hp)
            else:
                pri, task = heapq.heappop(self.hp)
                user = self.taskpri_to_user[(-pri, -task)]
                self.rmv(-task)
                return user
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
