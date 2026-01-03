class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        positive = 1
        if not s or (not (s[0].isdigit() or s[0] == '+' or s[0] == '-')):
            return 0
        if s[0] == '-':
            positive = -1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        res = ''
        for num in s:
            if num.isdigit():
                res += num
            else:
                break
        if not res:
            return 0
        res = positive * int(res)
        res = max(res, 0-2**(31))
        res = min(res, 2**31 - 1)
        return res
        

