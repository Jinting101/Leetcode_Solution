class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pairs = {}
        for i in range(len(nums)):
            x = nums[i] - i
            pairs[x] = pairs.get(x, 0) + 1
        vals = list(pairs.values())
        res, cur = 0, vals[-1]
        for i in range(len(vals)-2, -1, -1):
            res += cur*vals[i]
            cur += vals[i]
        return res