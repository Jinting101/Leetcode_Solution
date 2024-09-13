class Solution(object):
    def reverseWords(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\
        s = s.strip() + \ \
        res = \\
        temp = \\
        for i in s:
            if i != ' ':
                temp += i
            elif temp != \\:
                res = \ \ + temp + res
                temp = \\
        if res.startswith(' '):
            res = res[1:]
        return res