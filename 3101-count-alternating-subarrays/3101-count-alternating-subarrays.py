class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        cur = 0
        n = len(nums)
        res = n
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                cur += 1
                res += cur
            else:
                cur = 0

        return res
