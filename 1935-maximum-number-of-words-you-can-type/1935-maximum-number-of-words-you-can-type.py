class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        lst = text.split()
        res = 0
        for x in lst:
            if len([c for c in x if c in brokenLetters]) == 0:
                res += 1
        return res