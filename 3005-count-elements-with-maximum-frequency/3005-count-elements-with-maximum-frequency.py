class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        m = max(dic.values())
        return sum([y for x,y in dic.items() if y == m])