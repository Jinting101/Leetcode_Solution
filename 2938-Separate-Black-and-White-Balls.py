class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        num = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                num += 1
            else:
                res += num
        return res