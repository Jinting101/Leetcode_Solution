class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = []
        dic = {}
        res = ''
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        for x in dic:
            heapq.heappush(pq, (-ord(x), dic[x]))
        # o, count = heapq.heappop(pq)
        # cur_max, cur_max_cnt = chr(-o), count
        # res += cur_max * min(cur_max_cnt, repeatLimit)
        # cur_max_cnt -= repeatLimit
        cur_max, cur_max_cnt = '', 0
        while pq:
            o, count = heapq.heappop(pq)
            x = chr(-o)
            if cur_max_cnt > 0:
                res += x
                if count - 1 > 0:
                    heapq.heappush(pq, (o, count-1))
            else:
                cur_max, cur_max_cnt = chr(-o), count
            res += cur_max * min(cur_max_cnt, repeatLimit)
            cur_max_cnt -= repeatLimit
        return res
