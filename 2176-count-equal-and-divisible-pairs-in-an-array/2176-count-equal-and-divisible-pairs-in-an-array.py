class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = {x:[] for x in nums}
        for i,x in enumerate(nums):
            dic[x].append(i)
        res = 0
        for x, lst in dic.items():
            if len(lst) == 1:
                continue
            divisible, nondivisible = 0, 0
            for y in lst:
                if y % k == 0:
                    divisible += 1
                else:
                    nondivisible += 1
            res += divisible * (divisible - 1) // 2 + divisible * nondivisible
        return res