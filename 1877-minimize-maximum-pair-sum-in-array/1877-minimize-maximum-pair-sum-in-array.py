class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        res = float('-inf')
        nums.sort()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n-1-i]
            res = max(res, a+b)
        return res