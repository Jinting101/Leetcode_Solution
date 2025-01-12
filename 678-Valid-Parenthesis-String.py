class Solution:
    def checkValidString(self, s: str) -> bool:
        op, cp = 0, 0
        for x in s:
            if x == ')':
                op -= 1
            else:
                op += 1
            if op < 0:
                return False
        for x in s[::-1]:
            if x == '(':
                cp -= 1
            else:
                cp += 1
            if cp < 0:
                return False
        return True