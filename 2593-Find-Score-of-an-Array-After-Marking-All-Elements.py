class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = 0
        q = []
        seen = set()
        l = len(nums)
        for i,x in enumerate(nums):
            heapq.heappush(q, (x, i))
        while q:
            val, ind = heapq.heappop(q)
            if ind not in seen:
                res += val
                seen.add(ind)
                if ind > 0:
                    seen.add(ind-1)
                if ind < l-1:
                    seen.add(ind+1)
        return res