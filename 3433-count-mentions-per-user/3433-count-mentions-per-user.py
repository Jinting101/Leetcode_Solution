class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        hp = []
        events.sort(key=lambda x:(int(x[1]), -ord(x[0][0])))
        res = [0] * numberOfUsers
        online_map = {i:[1, -1] for i in range(numberOfUsers)}
        for m, time, ids in events:
            time = int(time)
            if m == "OFFLINE":
                ids = int(ids)
                avail_time = time+60
                heapq.heappush(hp, (avail_time, ids))
                online_map[ids][0] = 0
                online_map[ids][1] = avail_time
            else:
                while hp and hp[0][0] <= time:
                    t, uid = heapq.heappop(hp)
                    if t == online_map[uid][1]:
                        online_map[uid][0] = 1
                if ids == "ALL":
                    for i in range(numberOfUsers):
                        res[i] += 1
                elif ids == "HERE":
                    for uid, online in online_map.items():
                        if online[0]:
                            res[int(uid)] += 1
                else:
                    ids_lst = [int(x[2:]) for x in ids.split()]
                    for uid in ids_lst:
                        res[uid] += 1
        return res

# [1, 1, 1]
# {0:1, 1:0, 2;1}