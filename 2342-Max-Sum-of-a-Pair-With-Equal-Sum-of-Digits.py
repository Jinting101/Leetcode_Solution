class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            nsum = sum(map(int, list(str(x))))
            if nsum not in dic:
                dic[nsum] = []
            heapq.heappush(dic[nsum], -x)
        res = -1
        for x in dic:
            if len(dic[x]) > 1:
                cur = - heapq.heappop(dic[x]) - heapq.heappop(dic[x])
                res = max(res, cur)
        return res
