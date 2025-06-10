class Solution:
    def maxDifference(self, s: str) -> int:
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        odd, even = 0, float('inf')
        for x,y in dic.items():
            if y % 2 == 0:
                even = min(even, y)
            else:
                odd = max(odd, y)
        return odd-even