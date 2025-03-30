class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i,x in enumerate(s):
            dic[x] = i
        curmax, ind, n = 0, 0, len(s)
        res = []
        while ind < n:
            curmax = max(curmax, dic[s[ind]])
            if curmax == ind:
                res.append(ind+1)
            ind += 1
        for i in range(len(res)-1, 0, -1):
            res[i] = res[i] - res[i-1]
        return res