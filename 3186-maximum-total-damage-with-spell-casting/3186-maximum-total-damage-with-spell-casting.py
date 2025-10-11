class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        dic = {}
        for x in power:
            dic[x] = dic.get(x, 0) + 1
        lst = sorted(list(dic.keys()))
        res = [0] * len(lst)
        for i,x in enumerate(lst):
            res[i] += x * dic[x]
            curmax = 0
            for j in range(i-3, i):
                if j >= 0 and x-lst[j] > 2:
                    curmax = max(curmax, res[j])
            res[i] += curmax
            res[i] = max(res[i], res[max(0, i-1)])
        return res[-1]

