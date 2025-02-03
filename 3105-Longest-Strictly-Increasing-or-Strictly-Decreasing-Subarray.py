class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                res = max(res, dp[i])
        dp = [1] * n
        for i in range(n-1, 0, -1):
            if nums[i] < nums[i-1]:
                dp[i-1] = dp[i] + 1
                res = max(res, dp[i-1])
        return res