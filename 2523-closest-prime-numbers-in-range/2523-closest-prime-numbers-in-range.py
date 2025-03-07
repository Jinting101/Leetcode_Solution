class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left <= 2 and right >= 3:
            return [2, 3]
        def check(x):
            prime = True
            for i in range(2, x):
                if x % i == 0:
                    prime = False
                    break
            return prime
        
        prev, x = 0, left
        res = []
        while x <= right:
            if check(x):
                res.append(x)
                if x != prev and x - prev == 2:
                    return [prev, x]
                prev = x
                x += 2
            else:
                x += 1
        if len(res) <= 1:
            return [-1, -1]
        y = min(res[i]-res[i-1] for i in range(1, len(res)))
        for i in range(1, len(res)):
            if res[i] - res[i-1] == y:
                return [res[i-1], res[i]]

        
        # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, ... 59, 61, 65]