class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = abs(nums[0]-nums[-1])
        n = len(nums)
        for i in range(1, n):
            res = max(res, abs(nums[i]-nums[i-1]))
        return res