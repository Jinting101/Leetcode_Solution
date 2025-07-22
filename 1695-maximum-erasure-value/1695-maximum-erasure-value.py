class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        seen = set()
        res, cur = 0, 0
        while r < n:
            x = nums[r]
            while x in seen:
                seen.remove(nums[l])
                cur -= nums[l]
                l += 1
            cur += x
            res = max(res, cur)
            seen.add(x)
            r += 1
        return res

