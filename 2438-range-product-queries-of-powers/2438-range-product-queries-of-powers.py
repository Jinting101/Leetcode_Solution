class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        pows = []
        x = 1
        while x <= n:
            pows.append(x)
            x <<= 1
        lst = []
        if n in pows:
            lst.append(n)
        else:
            cur, ind = 0, len(pows) - 1
            while cur < n:
                if pows[ind] + cur <= n:
                    cur += pows[ind]
                    lst.append(pows[ind])
                ind -= 1
        lst = lst[::-1]
        psum = [1]
        for x in lst:
            psum.append(psum[-1] * x)
        res = []
        for st, ed in queries:
            res.append(psum[ed+1] // psum[st] % MOD)
        return res