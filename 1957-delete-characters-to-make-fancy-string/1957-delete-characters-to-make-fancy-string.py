class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        prev = s[0]
        for x in s[1:]:
            if x == prev:
                res += x
                prev += x
            elif len(prev) == 2 and x == prev[-1]:
                continue
            else:
                res += x
                prev = x
        return res


        ans = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                cnt += 1
                if cnt < 3:
                    ans += s[i]
            else:
                cnt = 1
                ans += s[i]
        return ans