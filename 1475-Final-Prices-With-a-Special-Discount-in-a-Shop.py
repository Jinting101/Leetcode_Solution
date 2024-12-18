class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        pq = [(l-1, prices[-1])]
        res = [x for x in prices]
        for i in range(l-2, -1, -1):
            while pq and pq[0][1] > prices[i]:
                heapq.heappop(pq)
            if pq and pq[0][1] <= prices[i]:
                res[i] -= pq[0][1]
            heapq.heappush(pq, (i, prices[i]))
        return res


        l = len(prices)
        res = [x for x in prices]
        for i in range(l):
            x = prices[i]
            for j in range(i+1, l):
                if prices[j] <= x:
                    res[i] = x - prices[j]
                    break
        return res