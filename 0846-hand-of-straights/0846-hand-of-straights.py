class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        dic = {}
        for x in hand:
            dic[x] = dic.get(x, 0) + 1
        for x in dic:
            l = dic[x]
            if l == 0:
                continue
            for y in range(x+1, x+groupSize):
                if y not in dic or dic[y] < l:
                    return False
                dic[y] -= l
        return True
