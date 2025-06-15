class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_replace = [x for x in s if x != '9']
        max_replace = '9' if not max_replace else max_replace[0]
        min_replace = s[0]
        if '0' not in s and s[0] == '1':
            min_replace = [x for x in s if x != s[0]]
            min_replace = '2' if not min_replace else min_replace[0]
        if '0' in s and s[0] == '1':
            for x in s[1:]:
                if x != '0' and x != '1':
                    min_replace = x
                    break
        
        if min_replace == s[0]:
            return int(s.replace(max_replace, '9')) - int(s.replace(min_replace, '1'))
        return int(s.replace(max_replace, '9')) - int(s.replace(min_replace, '0'))




        # 9024
        # 1004