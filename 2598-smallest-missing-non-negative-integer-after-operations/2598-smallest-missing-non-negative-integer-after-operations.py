class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        dic = {}
        for x in nums:
            num = x % value
            dic[num] = dic.get(num, 0) + 1
        res = set()
        for x in dic:
            for i in range(dic[x]):
                res.add(x+i*value)
        for i in range(10**5+2):
            if i not in res:
                return i
        return -1