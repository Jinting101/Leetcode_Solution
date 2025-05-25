class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
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