class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prev = res = nums[0]
        for x in nums[1:]:
            if x > 0 and x != prev:
                res += x
            prev = x
        return res