class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        for i in range(t):
            lst = sorted(list(dic.keys()))
            temp = {}
            for x in lst:
                if x != 'z':
                    temp[chr(ord(x) + 1)] = dic[x] % mod
                else:
                    temp['a'] = dic[x] % mod
                    temp['b'] = (temp.get('b', 0) + dic[x]) % mod
            dic = temp
        
        return sum(dic.values()) % mod

