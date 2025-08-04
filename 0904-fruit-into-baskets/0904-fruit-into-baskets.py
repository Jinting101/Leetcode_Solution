class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        l, n = 0, len(fruits)
        seen, cur = {}, 0
        for r in range(n):
            f = fruits[r]
            seen[f] = seen.get(f, 0) + 1
            if len(seen) > 2:
                removed = [x for x in seen if x != fruits[r-1]][0]
                while removed in seen and seen[removed] > 0:
                    seen[fruits[l]] -= 1
                    cur -= 1
                    l += 1
                seen.pop(removed)
            cur += 1
            res = max(res, cur)
        return res

