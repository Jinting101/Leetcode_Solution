class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vow = [0]*len(words)
        va = {'a', 'e', 'i', 'o', 'u'}
        for i,x in enumerate(words):
            st = x[0] in va
            ed = x[-1] in va
            if st and ed:
                vow[i] = 1
        for i,x in enumerate(vow):
            if i == 0:
                continue
            if x==0:
                vow[i] = vow[i-1]
            else:
                vow[i] += vow[i-1]
        res = []
        for x,y in queries:
            z = 0 if x == 0 else vow[x-1]
            res.append(vow[y]-z)
        return res

        vow = [0]*(len(words)+1)
        va = {'a', 'e', 'i', 'o', 'u'}
        for i,x in enumerate(words):
            ind = i + 1
            st = x[0] in va
            ed = x[-1] in va
            if st and ed:
                vow[ind] = 1
        for i,x in enumerate(vow):
            if i == 0:
                continue
            if x==0:
                vow[i] = vow[i-1]
            else:
                vow[i] += vow[i-1]
        res = []
        for x,y in queries:
            res.append(vow[y+1]-vow[x])
        return res
        