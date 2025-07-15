class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        cond1, cond2 = False, False
        for x in word:
            if x.isdigit():
                continue
            elif x.isalpha():
                if x.lower() in vowels:
                    cond1 = True
                else:
                    cond2 = True
            else:
                return False
        return cond1 and cond2 and len(word) > 2
            