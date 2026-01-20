class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(k):
            needed = 1
            cur = 0
            for x in weights:
                if cur + x <= k:
                    cur += x
                else:
                    needed += 1
                    cur = x
            return needed <= days
        
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l+r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
