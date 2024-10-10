class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ans = 0
        # n = len(nums)

        # # Create a list of tuples (element, index)
        # vp = [(nums[i], i) for i in range(n)]

        # # Sort the list based on the element values
        # vp.sort()

        # # Keep track of the minimum index seen so far
        # min_index = vp[0][1]

        # # Traverse the sorted list to calculate the maximum width ramp
        # for i in range(1, n):
        #     current_index = vp[i][1]
        #     ans = max(ans, current_index - min_index)
        #     min_index = min(min_index, current_index)

        # return ans


        ans = 0
        n = len(nums)

        # Stack to store the pairs of (value, index) in decreasing order
        st = []

        # First pass: store elements in decreasing order
        for i in range(n):
            if not st or st[-1][0] > nums[i]:
                st.append((nums[i], i))

        # Second pass: start from the last index to find the largest ramp
        for i in range(n - 1, -1, -1):
            while st and nums[i] >= st[-1][0]:
                index = st[-1][1]
                ans = max(ans, i - index)
                st.pop()

        return ans

# Monotonic Stack Construction:
# We iterate through the array from left to right, and for every index i, if the stack is empty or nums[i] is less than the value at the index on the top of the stack, we push the index i onto the stack. This helps to maintain a decreasing sequence of indices in terms of their nums values.

# Finding Maximum Width:
# After building the stack, we iterate the array from the end (j = n - 1) to the beginning. For each index j, we pop from the stack while the top of the stack has an index i such that nums[i] <= nums[j]. For every valid ramp, we calculate the width j - i and update the maximum width.

# Result: Once we've traversed the array, the maximum width will be stored in the maxWidth variable.



                