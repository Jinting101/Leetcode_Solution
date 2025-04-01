class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        dic = {}
        for x in hand:
            dic[x] = dic.get(x, 0) + 1
        dic = dict(sorted(dic.items(), key = lambda x : x[0]))
        for x in dic:
            l = dic[x]
            if l == 0:
                continue
            if l < 0:
                return False
            dic[x] -= l
            for i in range(1, groupSize):
                y = x + i
                if y not in dic:
                    return False
                dic[y] -= l
        return True