class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'
        for _ in range(9):
            l = len(s)
            for i in range(l):
                nxt = chr((ord(s[i]) + 1 - ord('a')) % 26 + ord('a'))
                s = s + nxt
        return s[k-1]