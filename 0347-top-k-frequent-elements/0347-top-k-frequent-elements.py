class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        lst = [(-x,y) for y,x in dic.items()]
        heapq.heapify(lst)
        res = []
        for i in range(k):
            res.append(heapq.heappop(lst)[1])
        return res