class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        # def rec(s):
        #     if "AB" not in s and "CD" not in s:
        #         return s
        #     else:
        #         i, l = 0, len(s)
        #         while i < l:
        #             if s[i:i+2] == "AB" or s[i:i+2] == "CD":
        #                 s = s[:i] + s[i+2:]
        #                 i += 2
        #             else:
        #                 i += 1
        #         return rec(s)
            
        # return len(rec(s))

        dic = {"B": "A", "D": "C"}
        top = []
        for i, x in enumerate(s):
            if top and x in dic and top[-1] == dic[x]:
                top.pop()
            else:
                top.append(x)
        return len(top)

        # relates to leetcode 20 - Valid parenthesis
        