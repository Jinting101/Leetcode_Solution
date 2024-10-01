class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """

        nums = [0] * k
        for num in arr:
            nums[num % k] += 1
        for idx in range(k):
            if idx == 0:
                if nums[idx] % 2 != 0:
                    return False
            elif nums[idx] != nums[k - idx]:
                return False
        return True


# For each number in the array, calculate its remainder when divided by ( k ). If the remainder is negative, convert it to a positive remainder by adding ( k ).

# Maintain a frequency array freq where freq[i] counts how many numbers in the array give a remainder of ( i ) when divided by ( k ).

# Divisible by ( k ): If a number has a remainder of ( 0 ), it must be paired with another number that also has a remainder of ( 0 ). Therefore, freq[0] should be even.

# Pairs of Remainders: For any remainder ( i ), it must be paired with ( k - i ). This means that freq[i] must equal freq[k - i].
# Specifically, for ( i = 1 ) to ( k ), check that freq[i] matches freq[k - i].

# If all conditions are satisfied, return true; otherwise, return false.

        