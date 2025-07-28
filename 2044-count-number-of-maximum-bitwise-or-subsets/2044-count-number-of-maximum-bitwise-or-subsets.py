class Solution:
    def backtrack(self, nums, index, currentOR, maxOR, count):
        if currentOR == maxOR:
            count[0] += 1
        
        for i in range(index, len(nums)):
            self.backtrack(nums, i + 1, currentOR | nums[i], maxOR, count)
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        
        # Step 1: Compute the maximum OR
        for num in nums:
            maxOR |= num
        
        count = [0]
        # Step 2: Backtrack to count the subsets
        self.backtrack(nums, 0, 0, maxOR, count)
        
        return count[0]

# Initialization:
# We first initialize the maxOR variable to store the bitwise OR of all elements in the array. This represents the highest OR value a subset can achieve.

# Backtracking Setup:
# We define a helper function backtrack that takes the current subset's OR value, the index to consider next, and updates the count when a subset achieves the maxOR.

# Base Case:
# Every time the current subset's OR equals maxOR, we increment the count because this subset is one of the valid subsets.

# Recursive Step:
# For each element in the array, we explore two options: either include the current element (update the OR) or skip it. This generates all possible subsets.

# Count Result:
# Once all subsets have been explored through backtracking, the count gives the number of subsets whose OR matches the maximum OR.