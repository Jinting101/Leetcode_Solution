class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cur, sl = 0, sum(nums)
        res = 0
        for x in nums[:-1]:
            cur += x
            sl -= x
            if cur >= sl:
                res += 1
        return res