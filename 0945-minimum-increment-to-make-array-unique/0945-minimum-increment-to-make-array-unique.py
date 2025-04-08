class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        lst = []
        for x in nums:
            lst.append(x)
        seen, n = set(), len(nums)
        res, curmax = 0, -1
        heapq.heapify(lst)
        for i in range(n):
            cur = heapq.heappop(lst)
            if cur not in seen:
                seen.add(cur)
                curmax = cur
            else:
                moves = abs(curmax-cur) + 1
                res += moves
                curmax = cur+moves
                seen.add(curmax)
        return res
