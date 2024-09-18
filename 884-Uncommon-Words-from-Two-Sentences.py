class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s = (s1 + ' ' + s2).split()
        seen = {}
        for x in s:
            if x not in seen:
                seen[x] = 0
            seen[x] += 1
        res = [x for x in seen if seen[x]==1]
        return res
        