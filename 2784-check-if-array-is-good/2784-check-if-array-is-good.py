class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if n != len(nums) - 1:
            return False
        dic = {}
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        for i in range(1, n+1):
            if (i != n) and (i not in dic or dic[i] != 1):
                return False
            if i == n and dic[i] != 2:
                return False
        return True
            