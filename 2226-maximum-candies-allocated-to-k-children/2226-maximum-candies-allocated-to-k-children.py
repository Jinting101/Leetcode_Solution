class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_distribute(cur):
            if cur == 0:
                return True
            res = 0
            for x in candies:
                res += x // cur
            return res >= k

        l, r = 0, max(candies)

        while l <= r:
            cur = l + (r-l) // 2
            if can_distribute(cur):
                l = cur + 1
            else:
                r = cur - 1
        
        return r