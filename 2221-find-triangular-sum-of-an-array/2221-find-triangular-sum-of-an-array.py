class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = nums.copy()
        l = len(res)
        while l > 1:
            temp = []
            for i in range(l-1):
                temp.append((res[i] + res[i+1]) % 10)
            res = temp
            l -= 1
        return res[0]