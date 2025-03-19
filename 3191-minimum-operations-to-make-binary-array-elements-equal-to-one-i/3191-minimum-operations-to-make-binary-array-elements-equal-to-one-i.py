class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res, l = 0, len(nums)
        for i in range(l-2):
            if nums[i] == 0:
                res += 1
                nums[i+1] = 1 if nums[i+1] == 0 else 0
                nums[i+2] = 1 if nums[i+2] == 0 else 0
            else:
                continue
        if nums[l-1] == 0 or nums[l-2] == 0:
            return -1
        return res