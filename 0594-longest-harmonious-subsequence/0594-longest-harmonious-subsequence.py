class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        dic = {}
        res = 0
        for i,x in enumerate(nums):
            if x not in dic:
                dic[x] = []
            elif len(dic[x]) > 1:
                dic[x].pop()
            dic[x].append(i)
        keys = list(dic.keys())
        for i in range(1, len(keys)):
            cur, prev = keys[i], keys[i-1]
            if cur - prev == 1:
                res = max(res, dic[cur][-1] - dic[prev][0] + 1)
        return res

