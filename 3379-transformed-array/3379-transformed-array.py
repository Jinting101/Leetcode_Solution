class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i, num in enumerate(nums):
            if num == 0:
                res[i] = num
            else num < 0:
                res[i] = nums[(i + num) % n]
                
        return res
