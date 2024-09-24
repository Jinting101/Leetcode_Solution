class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """

        # arr1_prefix = set()
        # max_length = 0

        # # Step 1: Build the prefix map for arr1
        # for num in arr1:
        #     str_num = str(num)
        #     prefix = ""
        #     for ch in str_num:
        #         prefix += ch
        #         arr1_prefix.add(prefix)
        
        # # Step 2: Check for common prefixes in arr2
        # for num in arr2:
        #     str_num = str(num)
        #     prefix = ""
        #     for ch in str_num:
        #         prefix += ch
        #         if prefix in arr1_prefix:
        #             max_length = max(max_length, len(prefix))
        
        # return max_length



        set1 = set()
        for num in set(arr1):
            while num and num not in set1:
                set1.add(num)
                num = num // 10
        
        ans = -1
        for num in set(arr2):
            while num:
                if num in set1:
                    ans = max(ans, num)
                    break

                num = num // 10
        
        return 0 if ans == -1 else len(str(ans))