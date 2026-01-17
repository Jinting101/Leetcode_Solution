class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n-1
        dp = [float('inf')] * n
        dp[-1] = 1
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                continue
            dp[i] = min(dp[i+1:i+1+nums[i]]) + 1
        return dp[0] - 1


        # 2 3 1 1 4
        # 3 2 3 2 1

        # dp[0] - 1

        # 2 3 0 1 4
        # 3 2 0 2 1