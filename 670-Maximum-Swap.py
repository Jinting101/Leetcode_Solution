import heapq
class Solution:
    def maximumSwap(self, num: int) -> int:
        # nums = [int(x) for x in str(num)]
        # pq = []
        # for i, x in enumerate(nums):
        #     heapq.heappush(pq, (-x, -i))
        # ind_x, ind_y = 0, 0
        # for i, x in enumerate(nums):
        #     negx, negi = heapq.heappop(pq)
        #     if negx != -x:
        #         ind_x, ind_y = i, -negi
        #         break
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[ind_y] == nums[i]:
        #         ind_y = i
        #         break
        # nums[ind_x], nums[ind_y] = nums[ind_y], nums[ind_x]
        # return int(''.join(map(str, nums)))

        # Convert the number to a list of characters for easy manipulation
        num_list = list(str(num))
        
        # Track the last occurrence of each digit (0-9)
        last = {int(d): i for i, d in enumerate(num_list)}
        
        # Traverse the number from left to right
        for i, digit in enumerate(num_list):
            # Check for a larger digit to swap
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Swap and return the new number
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(''.join(num_list))
        
        # If no swap occurred, return the original number
        return num

# Tracking last occurrence of digits:
# We iterate through the number's digits and store the last occurrence of each digit (0-9). This helps us quickly look up where a larger digit might be located in the number.

# Traversing the number:
# We traverse the digits of the number from left to right. For each digit, we check if there is any larger digit that appears after the current digit. If a larger digit exists, we can perform a swap to maximize the number.

# Performing a swap:
# As soon as we find a larger digit that can be swapped with the current digit, we perform the swap. This is done because we are allowed only one swap to maximize the number. After the swap, we return the new number immediately.

# Returning the result:
# If no swap was performed (because the number was already in its maximum form), we simply return the original number.