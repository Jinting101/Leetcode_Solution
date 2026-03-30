class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        c1 = Counter([x for i,x in enumerate(s1) if i % 2 == 0])
        c12 = Counter([x for i,x in enumerate(s2) if i % 2 == 0])
        c2 = Counter([x for i,x in enumerate(s1) if i % 2 == 1])
        c22 = Counter([x for i,x in enumerate(s2) if i % 2 == 1])
        return c1 == c12 and c2 == c22