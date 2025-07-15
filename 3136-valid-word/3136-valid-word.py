class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        cond1, cond2, cond3 = False, False, False
        for x in word:
            if x.isdigit():
                cond1 = True
            elif x.isalpha():
                if x.lower() in vowels:
                    cond2 = True
                else:
                    cond3 = True
            else:
                return False
        return cond1 and cond2 and cond3
            