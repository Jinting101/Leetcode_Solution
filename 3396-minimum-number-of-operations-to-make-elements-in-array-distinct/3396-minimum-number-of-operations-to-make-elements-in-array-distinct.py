class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        while not len(nums) == len(set(nums)):
            res += 1
            nums = nums[3:]
        return res