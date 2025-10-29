class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        lst = [(-y, x) for x,y in dic.items()]
        heapq.heapify(lst)
        res = []
        for _ in range(k):
            nf, num = heapq.heappop(lst)
            res.append(num)
        return res

        # {1:3, 2:2, 3:1}

        # [(-3, 1), (-2, 2), (-1, 3)]

        # O(n)
        # O(n log k)
        