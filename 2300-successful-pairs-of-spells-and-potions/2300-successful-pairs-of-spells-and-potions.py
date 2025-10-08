class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        cur, res = [], []
        for x in potions:
            rem = 1 if success % x != 0 else 0
            cur.append(success // x + rem)
        cur.sort()
        for x in spells:
            ind = bisect_right(cur, x)
            res.append(ind)
        return res

        