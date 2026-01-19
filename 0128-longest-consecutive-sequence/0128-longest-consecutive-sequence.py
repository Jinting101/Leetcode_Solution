class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for x in nums:
            if x-1 not in nums:
                l = 1
                while x + 1 in nums:
                    x += 1
                    l += 1
                res = max(res, l)
        return res