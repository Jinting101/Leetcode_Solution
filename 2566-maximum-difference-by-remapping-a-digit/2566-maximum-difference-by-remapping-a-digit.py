class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        min_replace = s[0]
        max_replace = [x for x in s if x != '9']
        max_replace = '9' if not max_replace else max_replace[0]
        return int(s.replace(max_replace, '9')) - int(s.replace(min_replace, '0'))

        
