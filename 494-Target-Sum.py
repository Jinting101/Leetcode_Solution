class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            add = backtrack(i + 1, total + nums[i])
            subtract = backtrack(i + 1, total - nums[i])
            memo[(i, total)] = add + subtract
            return memo[(i, total)]
        return backtrack(0, 0)

        def backtrack(lst, tar):
            if not lst:
                if tar == 0:
                    return 1
                return 0
            add = backtrack(lst[1:], tar-lst[0])
            subtract = backtrack(lst[1:], tar+lst[0])
            return add + subtract
        return backtrack(nums, target)