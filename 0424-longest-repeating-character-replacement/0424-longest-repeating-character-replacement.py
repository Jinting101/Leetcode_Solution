class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        def check(target):
            cur = 0
            l = 0
            used = 0
            res = 0
            for r in range(n):
                cur += 1
                if s[r] != target:
                    used += 1
                while used > k:
                    if s[l] != target:
                        used -= 1
                    cur -= 1
                    l += 1
                res = max(res, cur)
            return res

        ans = 0
        for i in range(ord("A"), ord("Z")+1):
            target = chr(i)
            ans = max(ans, check(target))
        
        return ans