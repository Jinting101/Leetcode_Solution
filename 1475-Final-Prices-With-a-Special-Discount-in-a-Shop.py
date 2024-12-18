class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        stack=[n-1]
        ans=[x for x in prices]
        for i in range(n-2, -1, -1):
            while stack and prices[i]<prices[stack[-1]]:
                stack.pop()
            if stack: ans[i]-=prices[stack[-1]]
            stack.append(i)
        return ans


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

