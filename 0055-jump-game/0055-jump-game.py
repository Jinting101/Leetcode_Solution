class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False


        n = len(nums)
        if len(nums) == 1:
            return True
        
        def dfs(idx):
            if nums[idx] == 0:
                return False
            if idx in memo:
                return memo[idx]
            if idx == n-1:
                memo[idx] = True
                return memo[idx]
            
            for i in range(idx + 1, idx + 1 + nums[idx]):
                if i < n and dfs(i):
                    memo[idx] = True
                    return memo[idx]
            
            memo[idx] = False
            return memo[idx]

        memo = {}
        return dfs(0)



