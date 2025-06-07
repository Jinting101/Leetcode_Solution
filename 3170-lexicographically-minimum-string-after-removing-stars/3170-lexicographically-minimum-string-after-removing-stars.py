class Solution:
    def clearStars(self, s: str) -> str:
        if '*' not in s:
            return s
        dic = {chr(ord('a')+i):[] for i in range(26)}
        res = list(s)
        for i,x in enumerate(s):
            if x != '*':
                dic[x].append(i)
            else:
                for cur_min in dic:
                    if dic[cur_min]:
                        pop_ind = dic[cur_min].pop()
                        res[pop_ind] = '*'
                        break
        return ''.join([x for x in res if x != '*'])

