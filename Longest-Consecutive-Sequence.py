class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def expand(x):
            res = 1
            if x+1 in snums:
                snums.remove(x+1)
                res += expand(x+1)
            if x-1 in snums:
                snums.remove(x-1)
                res += expand(x-1)
            return res
        if not nums:
            return 0
        snums = set(nums)
        res = 1
        for x in nums:
            if x in snums:
                snums.remove(x)
                cur = expand(x)
                res = max(res, cur)
        return res



        def expand(cur, x):
            if x+1 in snums:
                snums.remove(x+1)
                return expand(cur+1, x+1)
            if x-1 in snums:
                snums.remove(x-1)
                return expand(cur+1, x-1)
            return cur
        if not nums:
            return 0
        snums = set(nums)
        res = 1
        for x in nums:
            if x in snums:
                snums.remove(x)
                cur = expand(1, x)
                res = max(res, cur)
        return res
            



