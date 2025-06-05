class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dic_lst = [i for i in range(26)]
        for x,y in zip(s1, s2):
            ind1, ind2 = ord(x)-ord('a'), ord(y)-ord('a')
            cur_min = min(dic_lst[ind1], dic_lst[ind2])
            cur_max = max(dic_lst[ind1], dic_lst[ind2])
            for i in range(26):
                if dic_lst[i] == cur_max:
                    dic_lst[i] = cur_min
        res = []
        for x in baseStr:
            res.append(chr(ord('a') + dic_lst[ord(x)-ord('a')]))
        return ''.join(res)

