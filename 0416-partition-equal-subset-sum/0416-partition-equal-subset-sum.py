class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        n = len(nums)
        memo = {}
        def backtrack(num, ind):
            if (num, ind) in memo:
                return memo[(num, ind)]
            if ind >= n or num > target:
                return False
            if num == target:
                return True
            memo[(num, ind)] = backtrack(num+nums[ind], ind+1) or backtrack(num, ind+1)
            return memo[(num, ind)]
        return backtrack(0, 0)