class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def convert(x):
            cur = []
            for c in x:
                if c.lower() in v:
                    cur.append('_')
                else:
                    cur.append(c.lower())
            return ''.join(cur)

        v = set('aeiou')
        ws = set(wordlist)
        dic = {}
        for i,x in enumerate(wordlist):
            if x.lower() not in dic:
                dic[x.lower()] = i
            cur = convert(x)
            if cur not in dic:
                dic[cur] = i
        res = []
        for x in queries :
            y = x.lower()
            if x in ws:
                res.append(x)
            elif y in dic:
                res.append(wordlist[dic[y]])
            else:
                cur = convert(x)
                if cur in dic:
                    res.append(wordlist[dic[cur]])
                else:
                    res.append('')
        return res
        