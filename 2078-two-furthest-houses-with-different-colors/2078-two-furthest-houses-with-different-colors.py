class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        seen = set()
        dic = {}
        for i,x in enumerate(colors):
            dic[x] = i
        res = -1
        for i,x in enumerate(colors):
            if x in seen:
                continue
            for y in dic:
                if y != x and dic[y] > i:
                    res = max(res, dic[y] - i)
            seen.add(x)
        
        return res