class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def check(dic1, dic2):
            for x in dic1:
                if x not in dic2:
                    return False
                if dic1[x] != dic2[x]:
                    return False
            return True

        dicS = {}
        dicT = {}
        for x in s:
            dicS[x] = dicS.get(x, 0) + 1
        for x in t:
            dicT[x] = dicT.get(x, 0) + 1
        return check(dicS, dicT) and check(dicT, dicS)

        