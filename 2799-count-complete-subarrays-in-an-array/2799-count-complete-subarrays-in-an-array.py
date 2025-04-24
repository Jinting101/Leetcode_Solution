class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums) 
        cnt = len(set(nums))
        dic = {}
        res, l = 0, 0
        for r in range(n):
            dic[nums[r]] = dic.get(nums[r], 0) + 1
            while len(dic) == cnt:
                res += n - r
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    dic.pop(nums[l])
                l += 1
        return res