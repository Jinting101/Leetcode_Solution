class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = nums[0]
        for x in nums[1:]:
            cur = max(cur + x, x)
            res = max(cur, res)
        return res
