class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for x in nums:
            if x-1 not in nums:
                l = 1
                while x+1 in nums:
                    x = x + 1
                    l += 1
                res = max(l, res)
        return res