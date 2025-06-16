class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = nums[1] - nums[0]
        min_ele = nums[0]
        for x in nums[1:]:
            res = max(res, x-min_ele)
            min_ele = min(min_ele, x)
        if res <= 0:
            return -1
        return res