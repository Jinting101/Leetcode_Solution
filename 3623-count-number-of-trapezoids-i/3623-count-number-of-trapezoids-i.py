class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        dic = {}
        for x,y in points:
            dic[y] = dic.get(y, 0) + 1
        groups = []
        for x,cnt in dic.items():
            if cnt > 1:
                groups.append(cnt * (cnt-1) // 2)
        res = 0
        n, s = len(groups), sum(groups)
        for i,x in enumerate(groups):
            s -= x
            if i != n-1:
                res += x * s
        return res
        
