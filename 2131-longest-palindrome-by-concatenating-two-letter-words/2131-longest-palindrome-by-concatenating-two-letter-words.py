class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt, res, center = Counter(words), 0, False
        for w, c in cnt.items():
            rev = w[::-1]
            if w < rev and rev in cnt:
                res += 4 * min(c, cnt[rev])
            if w[0] == w[1]:
                res += 4 * (c // 2)
                if cnt[w] % 2:
                    center = True
        if center:
            res += 2
        return res



        res = 0
        dic = {}
        for x in words:
            dic[x] = dic.get(x, 0) + 1
        side, se, sidecnt, secnt = set(), {}, 0, 0
        for x in dic:
            if x in se or x in side or x[::-1] in side:
                continue
            if x[0] == x[1]:
                sidecnt += 4 * (dic[x] // 2)
                if dic[x] % 2 == 1: secnt = 2
            else:
                if x[::-1] in dic:
                    side.add(x)
                    side.add(x[::-1])
                    sidecnt += 4 * min(dic[x], dic[x[::-1]])
        return max(secnt, secnt+sidecnt)