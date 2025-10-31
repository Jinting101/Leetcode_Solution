class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        return [x for x in dic if dic[x] == 2]