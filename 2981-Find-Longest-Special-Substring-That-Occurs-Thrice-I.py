from collections import Counter
class Solution:
    def maximumLength(self, s: str) -> int:
        subarrays = []

        for i in range(len(s)):
            index = i
            while index < len(s) and s[index] == s[i]:
                subarrays.append(s[i:index+1])
                index += 1

        counter = Counter(subarrays)
        max_len = 0

        for j, n in counter.items():
            if n >= 3:
                if len(j) > max_len:
                    max_len = len(j)

        if max_len == 0:
            return -1
            
        return max_len

        def find(s, p):
            res = 0
            a, b = len(s), len(p)
            for i in range(0, a-b+1):
                if s[i:i+b] == p:
                    res += 1
            return res > 2
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        dic = {x:y for x,y in dic.items() if y > 2}
        if len(dic) == 0:
            return -1
        res = 1
        for x in dic:
            temp = x
            while find(s, x+temp):
                x += temp
            res = max(res, len(x))
        return res