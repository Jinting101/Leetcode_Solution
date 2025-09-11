class Solution:
    def sortVowels(self, s: str) -> str:
        lst = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for x in s:
            if x.lower() in vowels:
                lst.append(x)
        lst.sort(reverse=True)
        res = []
        for x in s:
            if x.lower() in vowels:
                res.append(lst.pop())
            else:
                res.append(x)
        return ''.join(res)