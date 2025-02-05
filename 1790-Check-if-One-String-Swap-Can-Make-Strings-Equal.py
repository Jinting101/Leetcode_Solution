class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # dic1, dic2, n = {}, {}, len(s1)
        # for i in range(n):
        #     dic1[s1[i]] = dic1.get(s1[i], 0) + 1
        #     dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        
        # if set(s1) != set(s2):
        #     return False
        a, b, swapped = '', '', False
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if s1[i] != s2[i] and not a and not swapped:
                a, b = s1[i], s2[i]
            elif s1[i] != s2[i] and a and not swapped:
                if a == s2[i] and b == s1[i]:
                    a = ''
                    swapped = True
                else:
                    return False
            else:
                return False
        return not a