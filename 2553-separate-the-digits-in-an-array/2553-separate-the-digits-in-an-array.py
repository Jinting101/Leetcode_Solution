class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            res.extend(list(map(int, list(str(x)))))
        return res