class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        res = check(tops[0])
        if res != -1:
            return res
        return check(bottoms[0])




        
        def check(target, top, bot):
            res = 0
            for i in range(n):
                if top[i] == target:
                    continue
                elif top[i] != target and bot[i] == target:
                    res += 1
                else:
                    return -1
            return res

        n = len(tops)
        dic = {}
        for x in tops+bottoms:
            dic[x] = dic.get(x, 0) + 1
        candidates = [x for x in dic if dic[x] >= n]
        if len(candidates) < 1:
            return -1
        target = candidates[0]
        moves1 = check(target, tops, bottoms)
        moves2 = check(target, bottoms, tops)
        if moves1 == moves2 and moves1 == -1:
            return -1
        elif moves1 == -1 or moves2 == -1:
            return max(moves1, moves2)
        else:
            return min(moves1, moves2)