class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = min(nums[0], nums[-1])
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo+hi) // 2
            if nums[lo] <= nums[mid]:
                res = min(res, nums[lo])
                lo = mid + 1
            else:
                hi = mid
        return res
