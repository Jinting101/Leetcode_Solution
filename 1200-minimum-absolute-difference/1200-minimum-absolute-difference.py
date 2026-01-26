class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        res = [[arr[0], arr[1]]]
        for i in range(1, n-1):
            a, b = arr[i], arr[i+1]
            diff = res[-1][1] - res[-1][0]
            if b - a == diff:
                res.append([a, b])
            elif b - a < diff:
                res = [[a, b]]
        return res