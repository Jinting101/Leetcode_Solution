class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        cnt = len([x for x in s if x in vowels])
        print(cnt)
        if cnt == 0:
            return False
        return True

        