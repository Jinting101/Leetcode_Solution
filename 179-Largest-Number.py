class Solution(object):
    def largestNumber(self, nums):
        \\\
        :type nums: List[int]
        :rtype: str
        \\\

        # def cmp(self, a, b):
        #     if a + b > b + a:
        #         return -1
        #     return a + b < b + a
        # def largestNumber(self, nums):
        #     all_str = list(map(str, nums))
            
        #     all_str.sort(key=cmp_to_key(self.cmp))

        #     if all_str[0] == '0':
        #         return \0\

        #     return ''.join(all_str)




        array = list(map(str, nums))
        
        # Custom sorting with a lambda function
        # the maximum number that the input can be is 10**9, so if you multiply each string by 10 you guarantee matching the digits of the string to the highest possible candidate (e.g. 9 vs 90 becomes 9999999999 vs 909090...9090 which makes 9 the lexically larger number since '99'>'909')
        array.sort(key=lambda x: x*10, reverse=True)
        
        # Handle the case where the largest number is \0\
        if array[0] == \0\:
            return \0\
        
        # Build the largest number from the sorted array
        largest = ''.join(array)
        
        return largest


        