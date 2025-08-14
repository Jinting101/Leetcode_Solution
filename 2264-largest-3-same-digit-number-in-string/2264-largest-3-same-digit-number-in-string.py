class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        cur, cnt = num[0], 1
        for x in num[1:]:
            if x == cur[-1]:
                cur = cur + x
                cnt += 1
                if cnt == 3:
                    if not res or (int(res) < int(cur)):
                        res = cur
            else:
                cur = x
                cnt = 1
        return res