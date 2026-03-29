class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (Counter([s1[0], s1[2]]) == Counter([s2[0], s2[2]])) and (Counter([s1[1], s1[3]]) == Counter([s2[1], s2[3]]))