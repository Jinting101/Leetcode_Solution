class Solution:
    def findXSum(self, nums: List[int], k: int, cnt: int) -> List[int]:
        dic = {}
        res = []
        for i,x in enumerate(nums):
            dic[x] = dic.get(x, 0) + 1
            if i >= k:
                dic[nums[i-k]] -= 1
            if i >= k-1:
                dic = dict(sorted(dic.items(), key = lambda x : (-x[1], -x[0])))
                lst = list(dic.keys())[:cnt]
                res.append(sum([y * dic[y] for y in lst]))
        return res
