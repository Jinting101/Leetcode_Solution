class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        lst = []
        cur = 0
        for x in nums:
            if x == 1:
                cur += 1
            else:
                lst.append(cur)
                cur = 0
        if cur:
            lst.append(cur)
        if len(lst) == 1:
            return lst[0] - 1
        res = [lst[i]+lst[i+1] for i in range(len(lst) - 1)]
        return max(res)