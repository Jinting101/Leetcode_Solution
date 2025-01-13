class Solution:
    def minimumLength(self, s: str) -> int:
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        res = 0
        for x in dic:
            if dic[x] <= 2:
                res += dic[x]
            elif dic[x] % 2 == 0:
                res += 2
            else:
                res += 1
        return res