class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(int)
        for i,x in enumerate(s):
            dic[x] = i
        res = []
        idx = 0
        prev = -1
        for i,x in enumerate(s):
            idx = max(idx, dic[x])
            if idx == i:
                res.append(idx - prev)
                prev = i
        return res
