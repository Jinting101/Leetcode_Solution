class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = max(nums)
        ans = 0
        cur_s = 0
        for i in range(len(nums)):
            if nums[i] == res:
                cur_s += 1
                ans = max(ans, cur_s)
            else:
                cur_s = 0
        return ans