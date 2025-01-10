class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        tar = [0]*26
        for y in words2:
            cur = [0]*26
            for x in y:
                cur[ord(x)-ord('a')] += 1
            for i,x in enumerate(cur):
                if x != 0:
                    tar[i] = max(tar[i], x)
        res = []
        for y in words1:
            ap = True
            cur = [0]*26
            for x in y:
                cur[ord(x)-ord('a')] += 1
            for i in range(26):
                if tar[i] > cur[i]:
                    ap = False
            if ap:
                res.append(y)
        return res