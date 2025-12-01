class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        prefix = 0
        for i,x in enumerate(nums):
            prefix += x
            target = prefix % k
            if target in dic and i - dic[target] >= 2:
                return True
            if target not in dic:
                dic[prefix % k] = i
        return False