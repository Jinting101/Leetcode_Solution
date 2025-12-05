class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        res = 0
        for r in range(len(s)):
            cur = s[r]
            while cur in seen:
                # if s[l] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(cur)
            res = max(res, r-l+1)
        return res