class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur = 0
        res = float('inf')
        for r,x in enumerate(nums):
            cur += x
            while cur >= target:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
