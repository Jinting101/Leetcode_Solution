class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        return len([x for x in dic if dic[x] % 2 == 1]) <= k and len(s) >= k