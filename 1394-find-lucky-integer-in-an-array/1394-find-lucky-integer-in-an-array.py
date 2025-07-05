class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        for x in arr:
            dic[x] = dic.get(x, 0) + 1
        lst = [x for x in dic if x == dic[x]]
        if not lst:
            return -1
        return max(lst)