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
        prev, prevnxt = nums[0], nums[0]
        for x in dic:
            if x - prev == 1:
                prevnxt = x
                res = max(res, dic[x][-1] - dic[prev][0] + 1)
            else:
                prev = prevnxt
                prevnxt = x
                if x - prev == 1:
                    res = max(res, dic[x][-1] - dic[prev][0] + 1)
        return res

