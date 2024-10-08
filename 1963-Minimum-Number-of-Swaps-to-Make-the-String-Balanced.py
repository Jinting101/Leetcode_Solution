class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # open_count, close_count = len(s) / 2, len(s) / 2
        
        # # Initialize variables
        # swaps = 0
        # open_diff = 0
        
        # # Traverse through the string
        # for c in s:
        #     if c == '[':
        #         open_diff += 1
        #     else:
        #         open_diff -= 1
            
        #     # If there are more ']' than '[', 
        #     # we need to swap the extra ']'
        #     if open_diff < 0:
        #         swaps += 1
        #         open_diff += 2
        
        # return swaps


        counter = 0
        for i in s:
            if i == '[':
                counter+=1
            else:
                if counter > 0:
                    counter -= 1
        return (counter +1) // 2