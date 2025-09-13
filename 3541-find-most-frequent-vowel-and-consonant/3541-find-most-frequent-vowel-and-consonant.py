class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        dic1, dic2 = {}, {}
        v1, v2 = 0, 0
        for x in s:
            if x in vowels:
                dic1[x] = dic1.get(x, 0) + 1
                v1 = max(v1, dic1[x])
            else:
                dic2[x] = dic2.get(x, 0) + 1
                v2 = max(v2, dic2[x])
        return v1+v2