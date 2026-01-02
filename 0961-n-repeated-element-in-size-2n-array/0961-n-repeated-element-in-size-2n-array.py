class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        n = len(nums) // 2
        return [x for x in dic if dic[x] == n][0]