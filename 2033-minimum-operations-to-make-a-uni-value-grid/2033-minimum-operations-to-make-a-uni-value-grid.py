class Solution:
    def minOperations(self, grid, x):
        values = sorted([val for row in grid for val in row])
        
        diff = [abs(val - values[0]) % x for val in values]
        if any(d != 0 for d in diff):
            return -1
        
        median = values[len(values) // 2]
        operations = sum(abs(val - median) // x for val in values)
        
        return operations

        
        # Create a list to store all the numbers from the grid
        nums_array = []
        result = 0

        # Flatten the grid into nums_array
        for row in grid:
            for num in row:
                nums_array.append(num)

        # Sort nums_array in non-decreasing order to easily find the median
        nums_array.sort()

        length = len(nums_array)
        # Store the median element as the final common value
        final_common_number = nums_array[length // 2]

        # Iterate through each number in nums_array
        for number in nums_array:
            # If the remainder when divided by x is different, return -1
            if number % x != final_common_number % x:
                return -1
            # Add the number of operations required to make the current number equal to final_common_number
            result += abs(final_common_number - number) // x

        return result