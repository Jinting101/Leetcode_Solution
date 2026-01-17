class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        used = 0
        cur = 0
        n = len(nums)
        for r in range(n):
            cur += 1
            if nums[r] == 0:
                used += 1
            while used > k:
                if nums[l] == 0:
                    used -= 1
                cur -= 1
                l += 1
            res = max(res, cur)
        return res