class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res, l = 0, len(nums)
        for i in range(2, l):
            x, y, z = nums[i-2], nums[i-1], nums[i]
            if x + y > z:
                res = max(res, x+y+z)
        return res