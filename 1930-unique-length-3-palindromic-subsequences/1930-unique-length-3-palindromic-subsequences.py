class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):  # Iterate over unique characters
            i, j = s.find(c), s.rfind(c)  # First and last occurrence
            if j > i + 1:  # Ensure there's at least one element between
                res += len(set(s[i+1:j]))  # Count unique middle elements
        return res


        res = set()
        dic = {}
        for i,x in enumerate(s):
            if x not in dic:
                dic[x] = []
            dic[x].append(i)
            if len(dic[x]) == 3:
                res.add(x*3)
            if len(dic[x]) >= 2:
                cur = set(s[dic[x][-2]+1:dic[x][-1]])
                for tx in cur:
                    res.add(x+tx+x)
        return len(res)
