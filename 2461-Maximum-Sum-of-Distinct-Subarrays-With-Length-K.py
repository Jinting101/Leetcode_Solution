class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        seen = set()
        res = 0
        cur = 0
        while r < len(nums):
            if nums[r] not in seen:
                cur += nums[r]
                seen.add(nums[r])
                if r - l + 1 == k:
                    res = max(res, cur)
                    cur -= nums[l]
                    seen.remove(nums[l])
                    l += 1
                r += 1
            else:
                while nums[r] in seen:
                    cur -= nums[l]
                    seen.remove(nums[l])
                    l += 1
        return res