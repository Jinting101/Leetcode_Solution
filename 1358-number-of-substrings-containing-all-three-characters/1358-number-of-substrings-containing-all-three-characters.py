class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {}
        res, l = 0, len(s)
        for i,x in enumerate(s):
            if x not in dic:
                dic[x] = []
            dic[x].append(i)
        for x in dic:
            dic[x] = dic[x][::-1]
        if 'a' not in dic or 'b' not in dic or 'c' not in dic:
            return 0
        while dic['a'] and dic['b'] and dic['c']:
            x,y,z = dic['a'][-1], dic['b'][-1], dic['c'][-1]
            res += l - max(x,y,z)
            if x < y and x < z:
                dic['a'].pop()
            elif y < x and y < z:
                dic['b'].pop()
            else:
                dic['c'].pop()
        # print(dic)
        return res