class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

        
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






