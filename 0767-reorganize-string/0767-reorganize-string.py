class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        lst = [(-y, x) for x,y in dic.items()]
        heapq.heapify(lst)
        res = ''
        while lst:
            neg, char = heapq.heappop(lst)
            res += char
            if neg != -1 and not lst:
                return ""
            if lst:
                neg2, char2 = heapq.heappop(lst)
                res += char2
                if neg != -1:
                    heapq.heappush(lst, (neg+1, char))
                if neg2 != -1:
                    heapq.heappush(lst, (neg2+1, char2))
        return res
            