class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        chars = []
        cur = ""
        num = 0
        for x in s:
            if x.isdigit():
                num = num * 10 + int(x)
            elif x == "[":
                nums.append(num)
                chars.append(cur)
                num = 0
                cur = ""
            elif x == "]":
                prev = chars.pop()
                cur = prev + cur * nums.pop()
            else:
                cur += x
        return cur