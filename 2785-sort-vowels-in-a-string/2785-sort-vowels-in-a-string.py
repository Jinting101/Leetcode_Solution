class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        dic = {x:0 for x in [y.upper() for y in vowels]+vowels}
        all_v = list(dic.keys())
        for x in s:
            if x in dic:
                dic[x] += 1
        res = []
        dic = {x:y for x,y in dic.items() if y != 0}
        for x in s:
            if x in all_v:
                for y in dic:
                    cur = y
                    dic[y] -= 1
                    if dic[y] == 0:
                        dic.pop(y)
                    break
                res.append(y)
            else:
                res.append(x)
        return ''.join(res)

