class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
    
        def backtrack(current):
            if len(current) == len(nums):
                perms.append(current[:])

            for n in nums:
                if n not in current:
                    current.append(n)
                    backtrack(current)
                    current.pop()
            
        backtrack([])
        return perms