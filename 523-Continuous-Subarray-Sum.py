class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_dict = {0: -1}
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            mod_value = prefix_sum % k

            if mod_value in mod_dict:
                if i - mod_dict[mod_value] > 1:
                    return True
            else:
                mod_dict[mod_value] = i
        
        return False