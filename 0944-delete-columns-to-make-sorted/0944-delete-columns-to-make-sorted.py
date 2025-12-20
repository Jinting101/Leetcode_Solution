class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        l = len(strs[0])
        lst = [[s[i] for s in strs] for i in range(l)]
        for col in lst:
            if col != sorted(col):
                res += 1
        return res