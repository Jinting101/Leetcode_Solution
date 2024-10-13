import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = float('-inf')
        
        # Initialize the heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, row, index)
            max_val = max(max_val, nums[i][0])  # Track the max element in the current range

        result = [-1e5, 1e5]  # Result initialized to a large possible range
        
        while min_heap:
            min_val, row, idx = heappop(min_heap)
            
            # Update the result range if the current range is smaller
            if max_val - min_val < result[1] - result[0]:
                result = [min_val, max_val]
            
            # Move to the next element in the same list (if any)
            if idx + 1 < len(nums[row]):
                next_val = nums[row][idx + 1]
                heapq.heappush(min_heap, (next_val, row, idx + 1))
                max_val = max(max_val, next_val)  # Update the max element
            else:
                # If any list is exhausted, we can stop since we can't form a valid range anymore
                break
        
        return result