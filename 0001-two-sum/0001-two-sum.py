class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,x in enumerate(nums):
            if target - x in dic:
                return [i, dic[target - x]]
            dic[x] = i
        return -1