class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        totalSum = sum(nums)
        rem = totalSum % p

        if rem == 0:
            return 0

        prefixMod = {0: -1}
        prefixSum = 0
        minLength = len(nums)

        for i, num in enumerate(nums):
            prefixSum += num
            currentMod = prefixSum % p
            targetMod = (currentMod - rem + p) % p

            if targetMod in prefixMod:
                minLength = min(minLength, i - prefixMod[targetMod])

            prefixMod[currentMod] = i

        return minLength if minLength < len(nums) else -1

# Total Sum Calculation:

# The total sum of the array is calculated to determine the remainder when divided by p.
# Example: For nums = [3, 1, 4, 2], the total sum is 10, and 10 % 6 = 4.
# Check if No Subarray is Needed:

# If the remainder is 0, no subarray needs to be removed, and we return 0 immediately.
# Prefix Sum with Modulo:

# As we iterate over the array, we calculate the prefix sum modulo p for each index.
# We store these modulo values in a hashmap for quick lookup. This helps us check if a previous prefix sum matches the required condition.
# Efficient Subarray Removal:

# For each element, we check if there exists a prefix sum modulo p that, when combined with the current prefix sum, would remove a subarray whose sum has the same remainder as rem.
# The hashmap allows us to do this efficiently by storing the indices of the prefix sums.
# Return Result:

# After the loop, we return the minimum length of the subarray found, or -1 if no valid subarray exists.